from django import forms
from django.forms import ModelForm

from .models import Organisation, Person


class OrganisationForm(ModelForm):
    class Meta:
        model = Organisation
        fields = ("name", "type", "location")


class PersonCreateForm(ModelForm):
    class Meta:
        model = Person
        fields = ("first_name", "surname", "email_address", "organisation")
        widgets = {
            "organisation": forms.Select(attrs={"class": "form-control"}),
        }
