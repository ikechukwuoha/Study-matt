from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import MyUserManager



class MyUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(max_length=50)
    name = models.CharField(max_length=200, null=True)
    phone_no = models.CharField(max_length=50)
    bio = models.TextField(null=True)
    avatar = models.ImageField(null=True, default='avatar.svg')
    date_joined = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    objects = MyUserManager()

    def __str__(self):
        return self.username