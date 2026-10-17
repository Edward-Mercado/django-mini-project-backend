from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name='index'),
    # calls the index function when called at path /
]