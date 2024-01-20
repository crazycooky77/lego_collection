from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import CustomUser, Collection, LegoCollection
from .forms import AddSet, CreateCollection, CreateSet, DeleteAccount, EditCollection, UpdateCol, UpdatePrivacy, UpdateUsername


class CreateUser(CreateView):
    """
    View for user creation
    Including CustomUser model and required user-input fields
    """
    model = CustomUser
    fields = ['username', 'email', 'privacy', 'password']
    template_name = 'signup.html'
    success_url = reverse_lazy('home')


def profile_widget(request):
    """
    Data for the mini profile widget
    To display number of sets owned and wishlist
    """
    col_id = Collection.objects.filter(
        collection_owner=request.user).values_list('collection_id',
                                                   flat=True)
    owned = LegoCollection.objects.filter(
        collection_id__in=col_id.all()).exclude(build_status='WL')
    wishlist = LegoCollection.objects.filter(
        collection_id__in=col_id.all(), build_status='WL')

    return owned, wishlist


def homepage_view(request):
    """
    View for the homepage
    If user is logged in, show set data for the profile widget
    Otherwise show login page
    """
    if request.user.is_authenticated:
        owned, wishlist = profile_widget(request)
        return render(request, 'index.html', {'owned': owned, 'wishlist': wishlist})
    else:
        return render(request, 'index.html')


def sort_filter_collection(request):
    """
    Function check for (reverse) sort and filter links
    Return sorted/filtered lego set results in the collection accordingly
    """
    col_id = Collection.objects.filter(
        collection_owner=request.user).values_list('collection_id',
                                                   flat=True)
    sort_by = None
    rsort_by = None
    filter_by = None

    # Check for sort, rsort, or filter in the page links
    try:
        sort_by = request.GET['sort']
    except:
        pass
    try:
        rsort_by = request.GET['rsort']
    except:
        pass
    try:
        filter_by = request.GET['filter']
    except:
        pass

    # If sort is in the link, get the next term to determine which field to sort on
    if sort_by is not None:
        if sort_by == 'nr':
            sets = LegoCollection.objects.filter(
                    collection_id__in=col_id.all()).order_by('set__set_number')
        elif sort_by == 'name':
            sets = LegoCollection.objects.filter(
                collection_id__in=col_id.all()).order_by('set__set_name')
        elif sort_by == 'pieces':
            sets = LegoCollection.objects.filter(
                collection_id__in=col_id.all()).order_by('set__nr_of_pieces')
        elif sort_by == 'status':
            sets = LegoCollection.objects.filter(
                collection_id__in=col_id.all()).order_by('build_status')
        elif sort_by == 'loc':
            sets = LegoCollection.objects.filter(
                collection_id__in=col_id.all()).order_by('set_location')
        elif sort_by == 'missing':
            sets = LegoCollection.objects.filter(
                collection_id__in=col_id.all()).order_by('missing_pieces')
        elif sort_by == 'fav':
            sets = LegoCollection.objects.filter(
                collection_id__in=col_id.all()).order_by('-favourited')
    # If rsort is in the link, get the next term to determine which field to reverse sort on
    elif rsort_by is not None:
        if rsort_by == 'nr':
            sets = LegoCollection.objects.filter(
                    collection_id__in=col_id.all()).order_by('-set__set_number')
        elif rsort_by == 'name':
            sets = LegoCollection.objects.filter(
                collection_id__in=col_id.all()).order_by('-set__set_name')
        elif rsort_by == 'pieces':
            sets = LegoCollection.objects.filter(
                collection_id__in=col_id.all()).order_by('-set__nr_of_pieces')
        elif rsort_by == 'status':
            sets = LegoCollection.objects.filter(
                collection_id__in=col_id.all()).order_by('-build_status')
        elif rsort_by == 'loc':
            sets = LegoCollection.objects.filter(
                collection_id__in=col_id.all()).order_by('-set_location')
        elif rsort_by == 'missing':
            sets = LegoCollection.objects.filter(
                collection_id__in=col_id.all()).order_by('-missing_pieces')
        elif rsort_by == 'fav':
            sets = LegoCollection.objects.filter(
                collection_id__in=col_id.all()).order_by('favourited')
    # If filter is in the link, get the next term to determine how to filter the data
    elif filter_by is not None:
        if filter_by == 'u500':
            sets = LegoCollection.objects.filter(
                collection_id__in=col_id.all(), set__nr_of_pieces__lt=500).order_by(
                'set__nr_of_pieces')
        elif filter_by == 'u1000':
            sets = LegoCollection.objects.filter(
                collection_id__in=col_id.all(), set__nr_of_pieces__lt=1000).order_by(
                'set__nr_of_pieces')
        elif filter_by == 'o500':
            sets = LegoCollection.objects.filter(
                collection_id__in=col_id.all(), set__nr_of_pieces__gt=500).order_by(
                '-set__nr_of_pieces')
        elif filter_by == 'o1000':
            sets = LegoCollection.objects.filter(
                collection_id__in=col_id.all(), set__nr_of_pieces__gt=1000).order_by(
                '-set__nr_of_pieces')
        elif filter_by == 'o2500':
            sets = LegoCollection.objects.filter(
                collection_id__in=col_id.all(), set__nr_of_pieces__gt=2500).order_by(
                '-set__nr_of_pieces')
        elif filter_by == 'o5000':
            sets = LegoCollection.objects.filter(
                collection_id__in=col_id.all(), set__nr_of_pieces__gt=5000).order_by(
                '-set__nr_of_pieces')
        elif filter_by == 'bnext':
            sets = LegoCollection.objects.filter(
                collection_id__in=col_id.all(), build_status='BN')
        elif filter_by == 'new':
            sets = LegoCollection.objects.filter(
                collection_id__in=col_id.all(), build_status='NEW')
        elif filter_by == 'stored':
            sets = LegoCollection.objects.filter(
                collection_id__in=col_id.all(), build_status='STORED')
        elif filter_by == 'wishlist':
            sets = LegoCollection.objects.filter(
                collection_id__in=col_id.all(), build_status='WL')
        elif filter_by == 'miss-yes':
            sets = LegoCollection.objects.filter(
                collection_id__in=col_id.all(), missing_pieces__isnull=False)
        elif filter_by == 'miss-no':
            sets = LegoCollection.objects.filter(
                collection_id__in=col_id.all(), missing_pieces__isnull=True)
        elif filter_by == 'fav-yes':
            sets = LegoCollection.objects.filter(
                collection_id__in=col_id.all(), favourited=1)
        elif filter_by == 'fav-no':
            sets = LegoCollection.objects.filter(
                collection_id__in=col_id.all(), favourited=0)
    # If no sort or filter is applicable, set default sorting
    else:
        sets = LegoCollection.objects.filter(
            collection_id__in=col_id.all()).order_by('-favourited',
                                                     'build_status')
    return sets


def collections_view(request):
    """
    View for collections page
    """
    if request.user.is_authenticated:
        owned, wishlist = profile_widget(request)
        if Collection.objects.filter(collection_owner__exact=request.user).exists():
            collection = Collection.objects.filter(
                collection_owner=request.user)

            sets = sort_filter_collection(request)

            if request.method == 'POST':
                if request.POST.get("delete-col-button"):
                    collection.delete()
        else:
            owned, wishlist = profile_widget(request)
            return render(request, 'collections.html', {'owned': owned, 'wishlist': wishlist})
        return render(request, 'collections.html',
                      {'collection': collection, 'sets': sets, 'owned': owned, 'wishlist': wishlist})
    else:
        return render(request, 'collections.html')


def profile_view(request):
    """
    View for the user's profile page
    """
    if request.user.is_authenticated:
        if request.method == 'POST':
            username_form = UpdateUsername(request.POST, instance=request.user)
            prv_form = UpdatePrivacy(request.POST, instance=request.user)
            del_form = DeleteAccount(request.POST)

            # Username change form functions
            if request.POST.get("username-button"):
                if username_form.is_valid():
                    username_form.save()
                    messages.success(request, 'Your username has been successfully updated')
                    return redirect(to='profile')
                else:
                    messages.error(request, "An account with that username already exists.")
            # Privacy settings change form function
            if request.POST.get("privacy-button"):
                if prv_form.is_valid():
                    prv_form.save()
                    messages.success(request, 'Your privacy settings have been successfully updated')
                    return redirect(to='profile')
            # Account deletion form function
            if request.POST.get("delete-button"):
                if del_form.is_valid():
                    CustomUser.delete(request.user)
                    logout(request)
                    messages.success(request, 'Account successfully deleted')
        else:
            col_id = Collection.objects.filter(
                collection_owner=request.user).values_list('collection_id',
                                                           flat=True)
            owned = LegoCollection.objects.filter(
                collection_id__in=col_id.all()).exclude(build_status='WL')
            wishlist = LegoCollection.objects.filter(
                collection_id__in=col_id.all(), build_status='WL')
            username_form = UpdateUsername(instance=request.user)
            prv_form = UpdatePrivacy(instance=request.user)
            del_form = DeleteAccount()
        return render(request, 'profile.html',
                      {'user_form': username_form, 'privacy_form': prv_form, 'del_form': del_form, 'owned': owned, 'wishlist': wishlist})
    else:
        return render(request, 'profile.html')


def shared_view(request):
    """
    View for the Shared page (not yet live)
    """
    if request.user.is_authenticated:
        owned, wishlist = profile_widget(request)
        return render(request, 'shared.html', {'owned': owned, 'wishlist': wishlist})
    else:
        return render(request, 'shared.html')


def create_collection(request):
    """
    View for creating a new collection
    """
    if request.user.is_authenticated:
        owned, wishlist = profile_widget(request)
        if request.method == 'POST':
            create_col_form = CreateCollection(request.POST, request.FILES)
            if request.POST.get("create-col-button"):
                if create_col_form.is_valid():
                    obj = create_col_form.save(commit=False)
                    obj.collection_owner = request.user
                    obj.save()
                    messages.success(request, 'Your collection has been successfully created.')
                    return redirect('collections')
        else:
            create_col_form = CreateCollection()
        return render(request, 'create_collection.html', {'create_col_form': create_col_form, 'owned': owned, 'wishlist': wishlist})
    else:
        return render(request, 'create_collection.html')


def edit_collection(request):
    """
    View for page to edit existing collections
    """
    if request.user.is_authenticated:
        if Collection.objects.filter(collection_owner__exact=request.user).exists():
            collection = Collection.objects.filter(
                collection_owner=request.user)
            col_id = Collection.objects.filter(
                collection_owner=request.user).values_list('collection_id',
                                                           flat=True)
            sets = LegoCollection.objects.filter(
                collection_id__in=col_id.all())

            if request.method == 'POST':
                edit_col_form = EditCollection(request.POST, request.FILES, instance=Collection.objects.get(pk=col_id[0]))
                update_col_form = [
                    UpdateCol(request.POST, prefix=str(set.id),
                              instance=LegoCollection.objects.get(
                                  pk=set.id)) for set in sets]
                if request.POST.get("update-col-button"):
                    if edit_col_form.is_valid():
                        edit_col_form.save()
                    for form in update_col_form:
                        set_del_pk = request.POST.getlist("delete-set")
                        if set_del_pk:
                            LegoCollection.objects.filter(pk__in=set_del_pk).delete()
                        if form.is_valid:
                            form.save()
                    messages.success(request, 'Collection updated successfully.')
                    return redirect(to='collections')
            else:
                owned, wishlist = profile_widget(request)
                edit_col_form = EditCollection(instance=Collection.objects.get(pk=col_id[0]))
                update_col_form = [
                    UpdateCol(prefix=str(set.id),
                              instance=LegoCollection.objects.get(
                                  pk=set.id)) for set in sets]
            return render(request, 'edit_collection.html',
                          {'form_set': zip(update_col_form, sets), 'edit_col_form': edit_col_form, 'collection': collection, 'sets': sets, 'owned': owned, 'wishlist': wishlist})
    else:
        return render(request, 'collections.html')


def create_set(request):
    """
    View for page to create a new lego set
    """
    if request.user.is_authenticated:
        owned, wishlist = profile_widget(request)
        if request.method == 'POST':
            create_set_form = CreateSet(request.POST, request.FILES)
            if request.POST.get("create-set-button"):
                if create_set_form.is_valid():
                    create_set_form.save()
                    messages.success(request, 'You successfully created a set. You can now search for and save it to your collection.')
                    return redirect('add_set')
        else:
            create_set_form = CreateSet()
        return render(request, 'create_set.html', {'create_set_form': create_set_form, 'owned': owned, 'wishlist': wishlist})
    else:
        return render(request, 'add_set.html')


def add_set(request):
    """
    View to add a lego set to an existing collection
    """
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
            owned, wishlist = profile_widget(request)
            add_set_form = AddSet()
        return render(request, 'add_set.html', {'add_set_form': add_set_form, 'owned': owned, 'wishlist': wishlist})
    else:
        return render(request, 'collections.html')
