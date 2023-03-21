from django.urls import path

from . import views
from .views import OrganisationCreateView, PersonCreateView

app_name = "basic"
urlpatterns = [
    path("", views.index, name="index"),
    path("add/", PersonCreateView.as_view(), name="person-add"),
    path("orgadd/", OrganisationCreateView.as_view(), name="organisation-add"),
]
