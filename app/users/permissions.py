# permissions

from rest_framework.permissions import AllowAny, BasePermission
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError
from users.models import CustomUser
from quizzes.models import Quiz
from django.contrib.auth import authenticate

""" 
# sample permission (from frazzetto project aezh):
class IsCourseInstructor(BasePermission): # defines the permission
    def has_permission(self, request, view): # defines function, receives request and view, returns bool
        if not request.user.is_authenticated: # not logged in = no good
            return False
        if request.method == "GET": # all users can get
            return True
        if request.method == "POST": 
            course_id = request.data.get("course")
            if not course_id: # no course id provided in the request = no good
                return False
            return Courses.objects.filter(id=course_id, instructor=request.user).exists()
            # gets all course models with the given id and the instructor being the user
            # if there is return true if not return false
        return False # catchback
"""