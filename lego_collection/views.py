from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import CustomUser
from .forms import UpdateUsername, UpdatePrivacy, DeleteAccount, CreateCollection, ViewCollection


# Create your views here.
def homepage_view(request):
    return render(request, 'index.html')


class CreateUser(CreateView):
    model = CustomUser
    fields = ['username', 'email', 'privacy', 'password']
    template_name = 'create_user.html'
    success_url = reverse_lazy('home')


def create_collection(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            create_col_form = CreateCollection(request.POST)
            if request.POST.get("create-col-button"):
                if create_col_form.is_valid():
                    obj = create_col_form.save(commit=False)
                    obj.collection_owner = request.user
                    obj.save()
                    messages.success(request, 'Your collection has been successfully created.')
                    return redirect('collections')
        else:
            create_col_form = CreateCollection()
        return render(request, 'create_collection.html', {'create_col_form': create_col_form})
    else:
        return render(request, 'create_collection.html')


def collections_view(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            view_col_form = ViewCollection(request.POST)

            if request.POST.get("create-col-button"):
                if view_col_form.is_valid():
                    view_col_form.save()
                    messages.success(request, 'Your collection has been successfully created.')
                    return redirect('collections')
        else:
            view_col_form = CreateCollection()
        return render(request, 'collections.html', {'view_col_form': view_col_form})
    else:
        return render(request, 'collections.html')


def profile_view(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            username_form = UpdateUsername(request.POST, instance=request.user)
            prv_form = UpdatePrivacy(request.POST, instance=request.user)
            del_form = DeleteAccount(request.POST)

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
            if request.POST.get("delete-button"):
                if del_form.is_valid():
                    CustomUser.delete(request.user)
                    logout(request)
                    messages.success(request, 'Account successfully deleted')
        else:
            username_form = UpdateUsername(instance=request.user)
            prv_form = UpdatePrivacy(instance=request.user)
            del_form = DeleteAccount()
        return render(request, 'profile.html',
                      {'user_form': username_form, 'privacy_form': prv_form, 'del_form': del_form})
    else:
        return render(request, 'profile.html')


def shared_view(request):
    return render(request, 'shared.html')
