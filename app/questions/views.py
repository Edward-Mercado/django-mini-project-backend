from django.shortcuts import render
from .serializers import QuestionSerializer
from .models import Question
from rest_framework import permissions, viewsets
from quizzes.permissions import IsTeacher

# Create your views here.

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all().order_by("id")
    serializer_class = QuestionSerializer
    
    def get_permissions(self):
        if self.action in ['get', 'list', 'retrieve']:
            permission_classes = [permissions.IsAuthenticated]
        else: 
            permission_classes = [IsTeacher]
            
        return [permission() for permission in permission_classes]