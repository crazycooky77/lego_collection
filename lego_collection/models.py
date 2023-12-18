from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.postgres.fields import ArrayField


class UserManager(BaseUserManager):
    def create_user(self, password=None, **extra_fields):
        extra_fields.setdefault('account_type', 'LC')
        user = self.model(**extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('account_type', 'LC')

        return self.create_user(**extra_fields)


# Create your models here
class CustomUser(AbstractUser):
    first_name = None
    last_name = None
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    privacy = models.CharField(max_length=20, default='Private')
    access = ArrayField(models.IntegerField(), default=None, blank=True, null=True)
    collection_id = models.IntegerField(default=None, blank=True, null=True)
    account_type = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)

    REQUIRED_FIELDS = ['email', 'privacy']

    objects = UserManager()

    def __str__(self):
        return self.username
