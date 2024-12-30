from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, login, password=None, email=None, **extra_fields):
        if not login:
            raise ValueError("The Login field must be set")
        email = self.normalize_email(email)
        user = self.model(login=login, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, login, password=None, email=None, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if not extra_fields.get('is_superuser'):
            raise ValueError("Superuser must have is_superuser=True.")
        if not extra_fields.get('is_staff'):
            raise ValueError("Superuser must have is_staff=True.")

        return self.create_user(login, password, email, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    login = models.CharField(max_length=255, unique=True, verbose_name="Логин",
                             error_messages={'unique': 'Это имя пользователя уже существует.'})
    password = models.CharField(max_length=255, verbose_name="Пароль")
    email = models.EmailField(blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "login"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["email"]

    objects = CustomUserManager()

    def __str__(self):
        return self.login
