from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('Please enter e-mail')
        elif not username:
            raise ValueError('Please enter username')
        user = self.model(
            username=username,
            email=email
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, password):
        user = self.create_user(
            username=username,
            email=email,
            password=password,
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user
    

class Users(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        max_length=250, unique=True,
        verbose_name='email'
    )
    username = models.CharField(max_length=100, verbose_name='username', unique=True)
    name = models.CharField(max_length=100, verbose_name='name', null=True)
    is_tutor = models.BooleanField(default=False, null=True)
    age = models.IntegerField(null=True)
    sex = models.CharField(max_length=30, null=True)
    country = models.CharField(max_length=100, verbose_name='country', null=True)
    description = models.TextField(max_length=300, null=True)
    introductory_video_link = models.URLField(null=True)
    icon = models.FileField(upload_to='icon/', default='icon/unknown_user.png')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username'] 

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'user'

    def __str__(self):
        return self.username