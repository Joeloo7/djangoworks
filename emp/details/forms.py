from django import forms
from details.models import employee
from django.forms import ModelForm

class DetailsForm(forms.ModelForm):
    class Meta:
        model=employee
        fields="__all__"