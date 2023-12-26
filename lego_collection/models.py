from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.postgres.fields import ArrayField
from django.utils.translation import gettext_lazy as _


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

    class Privacy(models.TextChoices):
        PRIVATE = 'PRV', _('Private')
        PUBLIC = 'PUB', _('Public')
        SHARED = 'SH', _('Shared')

    class Account(models.TextChoices):
        LC = 'LC', _('Lego Collection')
        FACEBOOK = 'FB', _('Facebook')
        GOOGLE = 'GGL', _('Google')

    first_name = None
    last_name = None
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    privacy = models.CharField(max_length=20, choices=Privacy.choices, default=Privacy.SHARED)
    collection_access = ArrayField(models.IntegerField(), default=None, blank=True, null=True)
    account_type = models.CharField(max_length=20, choices=Account.choices)
    is_active = models.BooleanField(default=True)

    REQUIRED_FIELDS = ['email', 'privacy']

    objects = UserManager()

    def __str__(self):
        return self.username


class LegoSet(models.Model):
    set_number = models.IntegerField(primary_key=True, unique=True)
    set_name = models.CharField(max_length=200)
    set_picture = models.ImageField(blank=True, null=True)
    nr_of_pieces = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = ['set_number']

    def __str__(self):
        return f'{self.set_number} | {self.set_name}'


class LegoCollection(models.Model):

    class Status(models.TextChoices):
        NEW = 'NEW', _('New (Owned)')
        BUILD_NEXT = 'BN', _('Build Next')
        STORED = 'STORED', _('Stored')
        WISH_LIST = 'WL', _('Wish List')

    collection_id = models.AutoField(primary_key=True)
    collection_name = models.CharField(max_length=100)
    collection_pic = models.ImageField(blank=True, null=True)
    collection_owner = models.OneToOneField('CustomUser', on_delete=models.CASCADE)
    set = models.ForeignKey('LegoSet', on_delete=models.CASCADE)
    missing_pieces = models.CharField(max_length=500, default=None, blank=True, null=True)
    build_status = models.CharField(max_length=50, choices=Status.choices)
    set_location = models.CharField(max_length=100, blank=True, null=True)
    favourited = models.BooleanField()
    shared = models.CharField(max_length=20, default=None, blank=True, null=True)

    class Meta:
        ordering = ['collection_id', 'build_status', 'set']

    def __str__(self):
        return f'{self.collection_id} | {self.collection_name}'
