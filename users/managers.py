from django.contrib.auth.models import BaseUserManager
from  . import models 

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, first_name=None, last_name=None):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        
        profile = models.Profile()
        profile.first_name = first_name
        profile.last_name = last_name
        profile.user = user

        profile.save()

        return user

    def create_superuser(self, email, password=None, first_name=None, last_name=None):
        user = self.create_user(
            email,
            password,
            first_name,
            last_name
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user