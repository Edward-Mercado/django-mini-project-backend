from django.shortcuts import render
from .serializers import QuestionSerializer
from .models import Question
from rest_framework import permissions, viewsets

# Create your views here.

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all().order_by("id")
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]