from django.contrib.auth import get_user_model
from django.utils import timezone
from rest_framework.response import Response
from rest_framework import permissions, generics
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from .tasks import reset_email_task
from .send_email import send_reset_email
import secrets
from . import serializers

User = get_user_model()


class RegistrationView(generics.CreateAPIView):
    serializer_class = serializers.RegisterSerializer
    permission_classes = (permissions.AllowAny,)


class LoginView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)


class ForgotPasswordView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = serializers.ForgotPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            email = serializer.data.get('email')
            user = User.objects.get(email=email)
            user.create_activation_code()
            user.password_reset_code_created_at = timezone.now()
            user.save()
            reset_email_task.delay(user.email, user.activation_code)
            return Response('Check your email! We sent a code!', status=200)
        except User.DoesNotExist:
            return Response('User with this email does not exist!', status=400)


class RestorePasswordView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = serializers.RestorePasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('Password changed successfully!')
