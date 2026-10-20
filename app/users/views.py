from django.contrib.auth.models import Group, User
from .models import CustomUser
from rest_framework import permissions, viewsets

from django.http import HttpResponse

from .serializers import UserSerializer