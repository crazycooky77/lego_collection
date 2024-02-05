from cloudinary.forms import CloudinaryFileField
from django import forms
from django.core.exceptions import ValidationError
from django.forms import ImageField, FileInput
from django_select2 import forms as s2forms
from .models import CustomUser, Collection, LegoCollection, LegoSet


class UpdateUsername(forms.ModelForm):
    """
    Form for updating usernames
    """
    username = forms.CharField(max_length=50, required=True,
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control'}))

    class Meta:
        model = CustomUser
        fields = ['username']

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            CustomUser.objects.get(username=username)
        except CustomUser.DoesNotExist:
            return username
        raise forms.ValidationError(
            "A user with that username already exists.")


class UpdatePrivacy(forms.ModelForm):
    """
    Form for updating user privacy
    """
    class Meta:
        model = CustomUser
        fields = ['privacy']


class DeleteAccount(forms.Form):
    """
    Form for deleting accounts
    """
    delete = forms.BooleanField(required=True)


class CreateCollection(forms.ModelForm):
    """
    Form to create collections
    """
    required_css_class = 'required'
    collection_pic = CloudinaryFileField(
        options={'crop': 'fit', 'max-width': 100, 'max-height': 100},
        required=False)

    class Meta:
        model = Collection
        fields = ['collection_name', 'collection_pic']


class EditCollection(forms.ModelForm):
    """
    Form for editing basic collection details
    """
    required_css_class = 'required'
    collection_pic = ImageField(widget=FileInput, required=False)

    class Meta:
        model = Collection
        fields = ['collection_name', 'collection_pic']


def validate_set_exists(value):
    """
    Function to raise a form ValidationError
    if a set number already exists during set creation
    """
    set = LegoSet.objects.filter(set_number=value)
    if set:
        raise ValidationError('This set number already exists. Please "Cancel" and search for it using "Add Set".')


class CreateSet(forms.ModelForm):
    """
    Form for creating new lego sets
    """
    required_css_class = 'required'
    set_number = forms.IntegerField(validators=[validate_set_exists])
    set_picture = CloudinaryFileField(
        options={'crop': 'fit', 'max-width': 100, 'max-height': 100},
        required=False)

    class Meta:
        model = LegoSet
        fields = ['set_number', 'set_name', 'set_picture', 'nr_of_pieces',
                  'lego_link']


class SetWidget(s2forms.ModelSelect2Widget):
    """
    Widget for AddSet form
    Enables a search field for all sets in the LegoSet database
    """
    search_fields = [
        'set_number__icontains',
        'set_name__icontains',
    ]


class AddSet(forms.ModelForm):
    """
    Form for adding sets to collections
    """
    required_css_class = 'required'

    class Meta:
        model = LegoCollection
        fields = ['set', 'build_status', 'set_location', 'favourited',
                  'missing_pieces']
        widgets = {'set': SetWidget()}


class UpdateCol(forms.ModelForm):
    """
    Form for updating sets in collections
    """
    class Meta:
        model = LegoCollection
        fields = ['build_status', 'set_location', 'missing_pieces',
                  'favourited']
