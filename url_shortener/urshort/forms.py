from urshort.models import *
from django import forms


class CreateNewShortUrl(forms.ModelForm):

    class Meta:
        model = ShortUrl
        fields = {"long_url"}
        widgets = {
            'long_url': forms.TextInput(attrs={"class": 'form-control'})
        }
