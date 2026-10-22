from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r"user", views.GetUserView)

urlpatterns = [
    path("", include(router.urls)),
    # calls the index function when called at path /
]