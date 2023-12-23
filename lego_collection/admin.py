from django.contrib import admin
from .models import CustomUser, LegoSet, LegoCollection


# Register your models here.
admin.site.register([CustomUser, LegoSet, LegoCollection])
