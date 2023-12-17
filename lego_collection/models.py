from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField


# Create your models here
class CustomUser(AbstractUser):
    user_id = models.IntegerField(unique=True)
    username = models.CharField(max_length=50, unique=True)
    email = models.CharField(max_length=100, unique=True)
    privacy = models.CharField(max_length=20, default='Private')
    access = ArrayField(models.IntegerField(), blank=True, null=True)
    collection_owner = models.IntegerField(blank=True, null=True)
    account_type = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    REQUIRED_FIELDS = ['user_id','email','privacy','account_type']