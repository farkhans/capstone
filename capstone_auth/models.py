from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from .utils import filepath
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, username, profile_img=None, password=None):
        user = self.model(username=username, profile_img=profile_img)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
class User(AbstractUser):
    profile_img = models.ImageField(upload_to=filepath, null=True, blank=True)

    objects = UserManager()