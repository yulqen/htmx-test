from django.forms import ModelForm
from . models import Person

class PersonCreateForm(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
