from django.contrib import admin
from .models import CustomUser, LegoSet, LegoCollection, Collection


# Admin site models
admin.site.register([CustomUser, LegoSet, LegoCollection, Collection])
