from django.contrib.auth.models import Group, User
from .models import Quiz
from rest_framework import permissions, viewsets

from .serializers import QuizSerializer
from .permissions import CanCreateQuiz, IsTeacher

# views are basically just api endpoints

class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all().order_by("name")
    serializer_class = QuizSerializer
    permission_classes = [permissions.IsAuthenticated, CanCreateQuiz, IsTeacher]
    
    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user)
    # bundles all of the http methods into one view "set"