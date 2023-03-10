from django.core.mail import send_mail
from django.utils import timezone
import secrets


def send_reset_email(user_email, code):
    send_mail('Letter with password reset code!', f"Your reset code:\n{code}", 'odecik30@gmail.com', [user_email, ],
              fail_silently=False)
