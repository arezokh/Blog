from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    age=models.PositiveIntegerField(null=True, blank=True)
    photo=models.ImageField(upload_to='photo/profiles/%Y/%m/%d',default='null')
    about=models.CharField(max_length=255, default='null')
    twitter_url=models.CharField( max_length=60, null=True, blank= True)
    instagram_url=models.CharField( max_length=60, null=True, blank= True)
    facebook_url=models.CharField( max_length=60, null=True, blank= True)