from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **kwargs):
        if not email:
            return ValueError('The given email must be set!')
        email = self.normalize_email(email=email)
        user = self.model(email=email, **kwargs)
        if user.type == 'student':
            user.is_mentor = False
            print(user.type)
        else:
            user.is_mentor = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **kwargs):
        kwargs.setdefault('is_staff', False)
        kwargs.setdefault('is_superuser', False)
        return self._create_user(email, password, **kwargs)

    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_active', True)
        if kwargs.get('is_staff') is not True:
            raise ValueError('Superuser must have status is_staff=True!')
        if kwargs.get('is_superuser') is not True:
            raise ValueError('Superuser must have status is_superuser=True!')
        return self._create_user(email, password, **kwargs)


class User(AbstractUser):
    EXPERIENCE_CHOICES = [
        ('personal', 'лично, частным образом'),
        ('professional', 'лично, профессионально'),
        ('online', 'онлайн'),
        ('other', 'другое'),
    ]

    AUDIENCE_CHOICES = [
        ('small', 'у меня маленькая аудитория'),
        ('enough', 'у меня достаточная аудитория'),
        ('no', 'в настоящий момент нет'),
    ]
    #
    USER_TYPE_CHOICES = [
        ('student', 'Student'),
        ('mentor', 'Mentor')
    ]
    email = models.EmailField('email address', unique=True)
    password = models.CharField(max_length=100)
    username = models.CharField(max_length=100, blank=True)
    type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='student')
    experience = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES, blank=True)
    audience = models.CharField(max_length=10, choices=AUDIENCE_CHOICES, blank=True)
    is_mentor = models.BooleanField()
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    activation_code = models.CharField(max_length=255, blank=True)
    password_reset_code_created_at = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def create_activation_code(self):
        import uuid
        code = str(uuid.uuid4())
        self.activation_code = code

    def __str__(self):
        return self.email
