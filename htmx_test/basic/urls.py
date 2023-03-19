from django.urls import path
from . views import PersonCreateView

from . import views

app_name = 'basic'
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', PersonCreateView.as_view(), name='person-add'),
]
