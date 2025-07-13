from django.db import models
from django.contrib.auth.models import AbstractUser


from django.contrib.auth.models import BaseUserManager


class ProfileManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email field must be filled')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('The <is_staff> value of superusers must be True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('The <is_superuser> value of superusers must be True')

        return self.create_user(email, password, **extra_fields)


class Profile(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
#    avatar = models.ImageField(upload_to='avatars/')
    google_id = models.CharField(max_length=255, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = ProfileManager()

    def __str__(self):
        return self.username
