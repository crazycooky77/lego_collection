from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import CustomUser, Collection, LegoCollection
from .forms import UpdateUsername, UpdatePrivacy, DeleteAccount, CreateCollection, CreateSet, AddSet, UpdateCol


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
        if Collection.objects.filter(collection_owner__exact=request.user).exists():
            collection = Collection.objects.filter(
                collection_owner=request.user)
            col_id = Collection.objects.filter(
                collection_owner=request.user).values_list('collection_id',
                                                           flat=True)
            sets = LegoCollection.objects.filter(
                collection_id__in=col_id.all())
        else:
            return render(request, 'collections.html')
        return render(request, 'collections.html',
                      {'collection': collection, 'sets': sets})
    else:
        return render(request, 'collections.html')


def edit_collection(request):
    if request.user.is_authenticated:
        if Collection.objects.filter(collection_owner__exact=request.user).exists():
            collection = Collection.objects.filter(
                collection_owner=request.user)
            col_id = Collection.objects.filter(
                collection_owner=request.user).values_list('collection_id',
                                                           flat=True)
            sets = LegoCollection.objects.filter(
                collection_id__in=col_id.all())

            update_col_form_post = [
                UpdateCol(request.POST, prefix=str(set.id),
                          instance=LegoCollection.objects.get(
                              pk=set.id)) for set in sets]
            update_col_form_get = [
                UpdateCol(prefix=str(set.id),
                          instance=LegoCollection.objects.get(
                              pk=set.id)) for set in sets]

            if request.method == 'POST':
                if request.POST.get("update-col-button"):
                    for form in update_col_form_post:
                        set_del_pk = request.POST.getlist("delete-set")
                        if set_del_pk:
                            LegoCollection.objects.filter(pk__in=set_del_pk).delete()
                        if form.is_valid:
                            form.save()
                    messages.success(request, 'Collection updated successfully.')
                    return redirect(to='collections')
            else:
                update_col_form_get
            return render(request, 'edit_collection.html',
                          {'form_set': zip(update_col_form_get, sets), 'collection': collection, 'sets': sets})
    else:
        return render(request, 'collections.html')


def create_set(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            create_set_form = CreateSet(request.POST, request.FILES)
            if request.POST.get("create-set-button"):
                if create_set_form.is_valid():
                    create_set_form.save()
                    messages.success(request, 'You successfully created a set. You can now search for and save it to your collection.')
                    return redirect('add_set')
        else:
            create_set_form = CreateSet()
        return render(request, 'create_set.html', {'create_set_form': create_set_form})
    else:
        return render(request, 'add_set.html')


def add_set(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            add_set_form = AddSet(request.POST)
            if request.POST.get("add-set-button"):
                if add_set_form.is_valid():
                    obj = add_set_form.save(commit=False)
                    collection = Collection.objects.filter(collection_owner=request.user).values_list('collection_id', flat=True)
                    obj.collection_id = collection
                    obj.save()
                    messages.success(request, 'Set successfully added to your collection.')
                    return redirect('collections')
        else:
            add_set_form = AddSet()
        return render(request, 'add_set.html', {'add_set_form': add_set_form})
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
