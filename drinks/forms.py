__author__ = 'john.back'

from django import forms

from drinks.models import Drink


class Order(forms.Form):
    drink = forms.ModelChoiceField(queryset=Drink.objects.all(), empty_label='Select yo drank!')
    person = forms.CharField(max_length=50)
    notes = forms.CharField(widget=forms.Textarea, required=False)

