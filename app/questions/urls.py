from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r"question", views.QuestionViewSet, basename='question')

urlpatterns = [
    path("", include(router.urls)),
    # calls the index function when called at path /
]