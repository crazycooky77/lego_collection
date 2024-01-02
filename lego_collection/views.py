from django.forms import forms
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import CustomUser
from .forms import UpdateUsername, UpdatePrivacy


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
            prv_form = UpdatePrivacy(request.POST, instance=request.user)

            if request.POST.get("username-button"):
                if username_form.is_valid():
                    username_form.save()
                    messages.success(request, 'Your username has been successfully updated')
                    return redirect(to='profile')
                else:
                    messages.error(request, "An account with that username already exists.")
            if request.POST.get("privacy-button"):
                if prv_form.is_valid():
                    prv_form.save()
                    messages.success(request, 'Your privacy settings have been successfully updated')
                    return redirect(to='profile')
        else:
            username_form = UpdateUsername(instance=request.user)
            prv_form = UpdatePrivacy(instance=request.user)
        return render(request, 'profile.html',
                      {'user_form': username_form, 'privacy_form': prv_form})
    else:
        return render(request, 'profile.html')


def shared_view(request):
    return render(request, 'shared.html')
