from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from . models import Person
from . forms import PersonCreateForm

def index(request):
    return render(request, 'basic/index.html')


class PersonCreateView(CreateView):
    model = Person
    form_class = PersonCreateForm
    success_url = reverse_lazy("basic:index")
