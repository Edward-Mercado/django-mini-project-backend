# permissions

from rest_framework.permissions import AllowAny, BasePermission
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError
from users.models import CustomUser
from quizzes.models import Quiz
from django.contrib.auth import authenticate

from rest_framework.permissions import BasePermission, SAFE_METHODS

class CanCreateQuiz(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        if request.method in SAFE_METHODS:
            return True

        return request.user.user_type == "TEACHER"

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.teacher == request.user
    
    from rest_framework.permissions import BasePermission

class IsTeacher(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.user_type == "TEACHER"
        )