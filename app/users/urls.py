from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet, basename='users')

urlpatterns = [
    path("register/", views.RegisterView.as_view(), name="register"),
    path("", include(router.urls)),
    # calls the index function when called at path /
]