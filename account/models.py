from django.db import models
from .managers import CustomUserManager
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.utils import timezone
import uuid

User = settings.AUTH_USER_MODEL

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_("Email Address"), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []    

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    username = models.CharField(max_length=20, unique=True, null=True, blank=True, default=f'user_{uuid.uuid1()}')
    bio = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.username