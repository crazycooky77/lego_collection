from cloudinary.forms import CloudinaryFileField
from django import forms
from django_select2 import forms as s2forms
from .models import CustomUser, Collection, LegoCollection, LegoSet


class UpdateUsername(forms.ModelForm):
    username = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = CustomUser
        fields = ['username']

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            CustomUser.objects.get(username=username)
        except CustomUser.DoesNotExist:
            return username
        raise forms.ValidationError("A user with that username already exists.")


class UpdatePrivacy(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['privacy']


class DeleteAccount(forms.Form):
    delete = forms.BooleanField(required=True)


class CreateCollection(forms.ModelForm):
    required_css_class = 'required'
    collection_pic = CloudinaryFileField(
        options={'crop': 'fit', 'width': 100, 'height': 100}, required=False)

    class Meta:
        model = Collection
        fields = ['collection_name', 'collection_pic']


class SetWidget(s2forms.ModelSelect2Widget):
    search_fields = [
        'set_number__icontains',
        'set_name__icontains',
    ]


class AddSet(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = LegoCollection
        fields = ['set', 'build_status', 'set_location', 'favourited', 'missing_pieces']
        widgets = {'set': SetWidget()}


class CreateSet(forms.ModelForm):
    required_css_class = 'required'
    set_picture = CloudinaryFileField(
        options={'crop': 'fit', 'width': 100, 'height': 100}, required=False)

    class Meta:
        model = LegoSet
        fields = ['set_number', 'set_name', 'set_picture', 'nr_of_pieces', 'lego_link']
