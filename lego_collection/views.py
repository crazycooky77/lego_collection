from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import CustomUser


# Create your views here.
def homepage_view(request):
    return render(request, 'index.html')


class CreateUser(CreateView):
    model = CustomUser
    fields = ['username', 'email', 'privacy', 'password']
    template_name = 'create_user.html'
    success_url = reverse_lazy('home')


def collections_view(request):
    return render(request, 'collections.html')


def profile_view(request):
    return render(request, 'profile.html')


def shared_view(request):
    return render(request, 'shared.html')