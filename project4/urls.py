"""
URL configuration for project4 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from lego_collection.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage_view, name='home'),
    path('', include('allauth.urls'), name='login'),
    path('add-set/', add_set, name='add_set'),
    path('collections/', collections_view, name='collections'),
    path('collections/?filter=<var>', collections_view, name='collections_filter'),
    path('collections/?rsort=<var>', collections_view, name='collections_rsort'),
    path('collections/?sort=<var>', collections_view, name='collections_sort'),
    path('create-set/', create_set, name='create_set'),
    path('create-collection/', create_collection, name='create_collection'),
    path('edit-collection/', edit_collection, name='edit_collection'),
    path('profile/', profile_view, name='profile'),
    path('select2/', include('django_select2.urls')),
    path('shared/', shared_view, name='shared'),
    path('sign-up/', CreateUser.as_view(), name='sign_up')
]
