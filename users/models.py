from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


# Create your models here.
class UserManger(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email field is required')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_admin', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('super user should has is_staff True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('super user should has is_superuser True')

        return self.create_user(username, email, password, **extra_fields)

    def create_customer(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_customer', True)

        return self.create_user(username, email, password, **extra_fields)


class User(AbstractUser):
    username = models.CharField(null=False, blank=False, unique=True, max_length=150)
    email = models.EmailField(null=False, blank=False, unique=True, max_length=128)
    password = models.CharField(null=False, blank=False, max_length=128)
    first_name = models.CharField(null=False, blank=True, max_length=50)
    last_name = models.CharField(null=False, blank=True, max_length=50)
    phone_name = models.CharField(null=False, blank=True, max_length=11)
    is_admin = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)

    objects = UserManger()

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'auth_user'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='UserProfile')
    username = User.username
    full_name = f"{User.first_name} {User.last_name}"
    profile_picture = models.ImageField(upload_to='profile_images/', blank=True, null=False)

    def __str__(self):
        return f"profile of {self.username}"

