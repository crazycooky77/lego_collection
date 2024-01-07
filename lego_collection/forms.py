from django import forms
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
    collection_name = forms.CharField(max_length=100, required=True)
    collection_pic = forms.ImageField(required=False)

    class Meta:
        model = Collection
        fields = ['collection_name', 'collection_pic']


class AddSet(forms.ModelForm):
    build_status = forms.ChoiceField()
    set_location = forms.CharField(max_length=100)
    favourited = forms.BooleanField()
    missing_pieces = forms.CharField(max_length=500)

    class Meta:
        model = LegoCollection
        fields = ['set', 'build_status', 'set_location', 'favourited', 'missing_pieces']


class CreateSet(forms.ModelForm):
    set_number = forms.IntegerField()
    set_name = forms.CharField(max_length=200)
    set_picture = forms.ImageField()
    nr_of_pieces = forms.IntegerField()

    class Meta:
        model = LegoCollection
        fields = ['set_number', 'set_name', 'set_picture', 'nr_of_pieces']
