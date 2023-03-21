from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import PersonCreateForm
from .models import Organisation, Person


def index(request):
    people = Person.objects.all()
    return render(request, "basic/index.html", context={"people": people})


class PersonCreateView(CreateView):
    model = Person
    form_class = PersonCreateForm
    success_url = reverse_lazy("basic:index")


class OrganisationCreateView(CreateView):
    model = Organisation
    fields = ["name", "type", "location"]
    template_name = "basic/organisation_create.html"
    success_url = reverse_lazy("basic:person-create")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.prefix = "org"

    def form_valid(self, form):
        response = super().form_valid(form)
        self.object.save()
        return response
