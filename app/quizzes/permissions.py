# permissions

from rest_framework.permissions import AllowAny, BasePermission
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError
from users.models import CustomUser
from quizzes.models import Quiz
from django.contrib.auth import authenticate

class CanCreateQuiz(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        
        if request.method in ["GET", "POST"]:
            return True
        
        if request.method == "DELETE":
            quiz_id = request.data.get("quiz")
            if not quiz_id:
                return False
            return Quiz.objects.filter(id=quiz_id, teacher=request.user).exists()
        
        return False
    
    def has_object_permission(self, request, view, obj):
        if request.method in ["DELETE", "PUT", "PATCH"]:
            return obj.teacher == request.method
        
        return False