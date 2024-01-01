from django.forms import forms
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import CustomUser
from .forms import UpdateUsername


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
    if request.user.is_authenticated:
        if request.method == 'POST':
            username_form = UpdateUsername(request.POST, instance=request.user)

            if username_form.is_valid():
                username_form.save()
                messages.success(request, 'Your username has been successfully updated')
                return redirect(to='profile')
            else:
                messages.error(request, "A user with that username already exists.")
        else:
            username_form = UpdateUsername(instance=request.user)
        return render(request, 'profile.html',
                      {'user_form': username_form})
    else:
        return render(request, 'profile.html')


def shared_view(request):
    return render(request, 'shared.html')
