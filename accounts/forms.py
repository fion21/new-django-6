from django import forms

from .models import Addprop


class AddpropForm(forms.ModelForm):
    class Meta:
        model = Addprop
        fields = ('city', 'description', 'price',
                  'photo_main', 'is_published', 'list_date')
