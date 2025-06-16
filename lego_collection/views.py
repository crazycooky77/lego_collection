import re
from django.contrib import messages
from django.contrib.auth import logout
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import CustomUser, Collection, LegoCollection
from .forms import (AddSet, CreateCollection, CreateSet, DeleteAccount,
                    EditCollection, UpdateCol, UpdateEmail, UpdatePrivacy,
                    UpdateUsername)


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
        return render(request, 'index.html',
                      {'owned': owned, 'wishlist': wishlist})
    else:
        return render(request, 'index.html')


def get_search_value(request):
    if request.POST.get('reset-sort') or request.POST.get('reset-filter') or request.POST.get('reset-search') or request.POST.get('empty-reset'):
        request.session['search_by'] = None
    elif request.POST.get('search-value'):
        request.session['search_by'] = request.POST['search-value']
    elif request.path == '/collections/' and '/collections' not in request.META.get('HTTP_REFERER') and request.session.get('search_by'):
        request.session['search_by'] = None
    else:
        request.session['search_by'] = request.session.get('search_by', None)
    search_by = request.session['search_by']

    if search_by is not None and not re.match(r'^(?=(?:.*\S.*){2,})[A-Za-z0-9- ]+$', search_by):
        search_by = 'INVALID_SEARCH'
    elif request.POST.get('search-button') and search_by is None:
        search_by = 'INVALID_SEARCH'
    return search_by


def sort_filter_collection(request, search_by = None):
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
    except MultiValueDictKeyError:
        pass
    try:
        rsort_by = request.GET['rsort']
    except MultiValueDictKeyError:
        pass
    try:
        filter_by = request.GET['filter']
    except MultiValueDictKeyError:
        pass

    # If search-value was POSTed, filter sets by the search term
    if search_by is not None and search_by != 'INVALID_SEARCH':
        if search_by.upper() in 'NEW (OWNED)':
            bstatus = 'NEW'
        elif search_by.upper() in 'BUILD NEXT':
            bstatus = 'BN'
        elif search_by.upper() in 'BUILT':
            bstatus = 'B'
        elif search_by.upper() in 'STORED':
            bstatus = 'STORED'
        elif search_by.upper() in 'EXTRA':
            bstatus = 'EX'
        elif search_by.upper() in 'WISH LIST':
            bstatus = 'WL'
        else:
            bstatus = None

        sets = LegoCollection.objects.filter(
            Q(collection_id__in=col_id.all()),
            Q(set__set_name__icontains=search_by) |
            Q(set__set_number__icontains=search_by) |
            Q(set_location__icontains=search_by) |
            Q(build_status=bstatus))
    else:
        sets = LegoCollection.objects.filter(
            collection_id__in=col_id.all())

    # If sort is in the link, get next term to determine which field to sort on
    if sort_by is not None:
        if sort_by == 'nr':
            sets = sets.order_by('set__set_number')
        elif sort_by == 'name':
            sets = sets.order_by('set__set_name')
        elif sort_by == 'pieces':
            sets = sets.order_by('set__nr_of_pieces')
        elif sort_by == 'status':
            sets = sets.order_by('build_status')
        elif sort_by == 'loc':
            sets = sets.order_by('set_location')
        elif sort_by == 'missing':
            sets = sets.order_by('missing_pieces')
        elif sort_by == 'fav':
            sets = sets.order_by('-favourited')
    # If rsort is in the link, get next term for the field to reverse sort on
    elif rsort_by is not None:
        if rsort_by == 'nr':
            sets = sets.order_by('-set__set_number')
        elif rsort_by == 'name':
            sets = sets.order_by('-set__set_name')
        elif rsort_by == 'pieces':
            sets = sets.order_by('-set__nr_of_pieces')
        elif rsort_by == 'status':
            sets = sets.order_by('-build_status')
        elif rsort_by == 'loc':
            sets = sets.order_by('-set_location')
        elif rsort_by == 'missing':
            sets = sets.order_by('-missing_pieces')
        elif rsort_by == 'fav':
            sets = sets.order_by('favourited')
    # If filter is in the link, get next term to determine how to filter data
    elif filter_by is not None:
        if filter_by == 'u500':
            sets = (sets.filter(
                set__nr_of_pieces__lt=500).order_by('set__nr_of_pieces'))
        elif filter_by == 'u1000':
            sets = sets.filter(
                set__nr_of_pieces__lt=1000).order_by('set__nr_of_pieces')
        elif filter_by == 'o500':
            sets = sets.filter(
                set__nr_of_pieces__gt=500).order_by('-set__nr_of_pieces')
        elif filter_by == 'o1000':
            sets = sets.filter(
                set__nr_of_pieces__gt=1000).order_by('-set__nr_of_pieces')
        elif filter_by == 'o2500':
            sets = sets.filter(
                set__nr_of_pieces__gt=2500).order_by('-set__nr_of_pieces')
        elif filter_by == 'o5000':
            sets = sets.filter(
                set__nr_of_pieces__gt=5000).order_by('-set__nr_of_pieces')
        elif filter_by == 'bnext':
            sets = sets.filter(build_status='BN')
        elif filter_by == 'built':
            sets = sets.filter(build_status='B')
        elif filter_by == 'extra':
            sets = sets.filter(build_status='EX')
        elif filter_by == 'new':
            sets = sets.filter(build_status='NEW')
        elif filter_by == 'stored':
            sets = sets.filter(build_status='STORED')
        elif filter_by == 'wishlist':
            sets = sets.filter(build_status='WL')
        elif filter_by == 'loc-yes':
            sets = sets.filter(set_location__isnull=False)
        elif filter_by == 'loc-no':
            sets = sets.filter(set_location__isnull=True)
        elif filter_by == 'miss-yes':
            sets = sets.filter(missing_pieces__isnull=False)
        elif filter_by == 'miss-no':
            sets = sets.filter(missing_pieces__isnull=True)
        elif filter_by == 'fav-yes':
            sets = sets.filter(favourited=1)
        elif filter_by == 'fav-no':
            sets = sets.filter(favourited=0)

    # If no sort/filter/search is applicable, set default sorting
    else:
        sets = sets.order_by('-favourited', 'build_status')

    sorted_sets = Paginator(sets, 50)
    page_number = request.GET.get('page')
    paginated_sets = sorted_sets.get_page(page_number)

    return sorted_sets, page_number, paginated_sets


def collections_view(request):
    """
    View for collections page
    """
    if request.user.is_authenticated:
        owned, wishlist = profile_widget(request)
        if Collection.objects.filter(
                collection_owner__exact=request.user).exists():
            collection = Collection.objects.filter(
                collection_owner=request.user)

            search_by = get_search_value(request)
            sets, page_number, paginated_sets = sort_filter_collection(request, search_by)
            if request.method == 'POST':
                if request.POST.get("delete-col-button"):
                    request.session['search_by'] = None
                    collection.delete()
                    messages.success(request,
                                     'Collection successfully deleted')
        else:
            owned, wishlist = profile_widget(request)
            return render(request, 'collections.html',
                          {'owned': owned, 'wishlist': wishlist})
        return render(request, 'collections.html',
                      {'collection': collection,
                       'sets': paginated_sets,
                       'owned': owned,
                       'wishlist': wishlist,
                       'search_by': search_by})
    else:
        return render(request, 'collections.html')


def profile_view(request):
    """
    View for the user's profile page
    """
    if request.user.is_authenticated:
        col_id = Collection.objects.filter(
            collection_owner=request.user).values_list('collection_id',
                                                       flat=True)
        owned = LegoCollection.objects.filter(
            collection_id__in=col_id.all()).exclude(build_status='WL')
        wishlist = LegoCollection.objects.filter(
            collection_id__in=col_id.all(), build_status='WL')
        if request.method == 'POST':
            username_form = UpdateUsername(request.POST, instance=request.user)
            email_form = UpdateEmail(request.POST, instance=request.user)
            prv_form = UpdatePrivacy(request.POST, instance=request.user)
            del_form = DeleteAccount(request.POST)

            # Username change form functions
            if request.POST.get("username-button"):
                if username_form.is_valid():
                    username_form.save()
                    messages.success(
                        request, 'Your username has been successfully updated')
                    return redirect(to='profile')
                else:
                    messages.error(
                        request,
                        "An account with that username already exists.")
                    username_form = UpdateUsername(instance=request.user)
                    email_form = UpdateEmail(instance=request.user)
                    prv_form = UpdatePrivacy(instance=request.user)
                    del_form = DeleteAccount()
            # Email change form functions
            if request.POST.get("profile-email-button"):
                if email_form.is_valid():
                    email_form.save()
                    messages.success(
                        request,
                        'Your email address has been successfully updated')
                    return redirect(to='profile')
                else:
                    messages.error(
                        request,
                        "An account with that email address already exists.")
                    username_form = UpdateUsername(instance=request.user)
                    email_form = UpdateEmail(instance=request.user)
                    prv_form = UpdatePrivacy(instance=request.user)
                    del_form = DeleteAccount()
            # Privacy settings change form function
            if request.POST.get("privacy-button"):
                if prv_form.is_valid():
                    prv_form.save()
                    messages.success(
                        request,
                        'Your privacy settings have been successfully updated')
                    return redirect(to='profile')
            # Account deletion form function
            if request.POST.get("delete-button"):
                if del_form.is_valid():
                    CustomUser.delete(request.user)
                    logout(request)
                    messages.success(request, 'Account successfully deleted')
        else:
            username_form = UpdateUsername(instance=request.user)
            email_form = UpdateEmail(instance=request.user)
            prv_form = UpdatePrivacy(instance=request.user)
            del_form = DeleteAccount()
        return render(request, 'profile.html',
                      {'user_form': username_form,
                       'email_form': email_form,
                       'privacy_form': prv_form,
                       'del_form': del_form, 'owned': owned,
                       'wishlist': wishlist})
    else:
        return render(request, 'profile.html')


def shared_view(request):
    """
    View for the Shared page (not yet live)
    """
    if request.user.is_authenticated:
        owned, wishlist = profile_widget(request)
        return render(request, 'shared.html',
                      {'owned': owned, 'wishlist': wishlist})
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
                    messages.success(
                        request,
                        'Your collection has been successfully created.')
                    return redirect('collections')
        else:
            create_col_form = CreateCollection()
        return render(request, 'create_collection.html',
                      {'create_col_form': create_col_form, 'owned': owned,
                       'wishlist': wishlist})
    else:
        return render(request, 'create_collection.html')


def edit_collection(request):
    """
    View for page to edit existing collections
    """
    if request.user.is_authenticated:
        owned, wishlist = profile_widget(request)
        if Collection.objects.filter(
                collection_owner__exact=request.user).exists():
            collection = Collection.objects.filter(
                collection_owner=request.user)
            col_id = Collection.objects.filter(
                collection_owner=request.user).values_list('collection_id',
                                                           flat=True)
            search_by = get_search_value(request)
            sets, page_number, paginated_sets = sort_filter_collection(request, search_by)

            if request.method == 'POST':
                edit_col_form = EditCollection(request.POST, request.FILES,
                                               instance=Collection.objects.get(pk=col_id[0]))
                update_col_form = [
                    UpdateCol(request.POST, prefix=str(lset.id),
                              instance=LegoCollection.objects.get(
                                  pk=lset.id)) for lset in paginated_sets]

                if request.POST.get('update-col-button') or request.POST.get('update-con-col-button'):
                    for form in update_col_form:
                        if form.is_valid():
                            set_del_pk = request.POST.getlist('delete-set')
                            form.save()
                            LegoCollection.objects.filter(
                                pk__in=set_del_pk).delete()
                    if edit_col_form.is_valid():
                        edit_col_form.save()
                        messages.success(request,
                                         'Collection updated successfully.')
                        if request.POST.get('update-col-button'):
                            del request.session['search_by']
                            return redirect(to='collections')
                        elif request.POST.get('update-con-col-button'):
                            del request.session['search_by']
                            return redirect(to='edit_collection')

            edit_col_form = EditCollection(instance=Collection.objects.get(
                pk=col_id[0]))
            update_col_form = [
                UpdateCol(prefix=str(lset.id),
                          instance=LegoCollection.objects.get(
                              pk=lset.id)) for lset in paginated_sets]

            return render(request, 'edit_collection.html',
                          {'form_set': zip(update_col_form, paginated_sets),
                           'edit_col_form': edit_col_form,
                           'collection': collection, 'sets': paginated_sets,
                           'owned': owned, 'wishlist': wishlist,
                           'search_by': search_by})
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
                    messages.success(
                        request,
                        'You successfully created a set. You can' +
                        ' now search for and save it to your collection.')
                    return redirect('add_set')
        else:
            create_set_form = CreateSet()
        return render(request, 'create_set.html',
                      {'create_set_form': create_set_form, 'owned': owned,
                       'wishlist': wishlist})
    else:
        return render(request, 'create_set.html')


def add_set(request):
    """
    View to add a lego set to an existing collection
    """
    if request.user.is_authenticated:
        owned, wishlist = profile_widget(request)
        if request.method == 'POST':
            add_set_form = AddSet(request.POST)
            if request.POST.get("add-set-button"):
                if add_set_form.is_valid():
                    obj = add_set_form.save(commit=False)
                    collection = Collection.objects.filter(
                        collection_owner=request.user).values_list(
                        'collection_id', flat=True)
                    obj.collection_id = collection
                    obj.save()
                    messages.success(
                        request, 'Set successfully added to your collection.')
                    return redirect('collections')
        else:
            add_set_form = AddSet()
        return render(request, 'add_set.html',
                      {'add_set_form': add_set_form, 'owned': owned,
                       'wishlist': wishlist})
    else:
        return render(request, 'collections.html')
