from typing import Iterable
from django.db import models
from . import managers
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin

class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(
        unique=True,
        max_length=255,
    )

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True) 
    created_at = models.DateTimeField(auto_now=True) 

    objects =  managers.UserManager()

    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        return self.is_admin

class Profile(models.Model):
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    image = models.ImageField()

    def __str__(self):
        return f"profile for {self.user.email}"
