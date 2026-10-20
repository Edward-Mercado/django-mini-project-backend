from django.db import models
from django.utils import timezone

# Create your models here.

class Quiz(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    due_date = models.DateTimeField()
    teacher = models.ForeignKey("users.") #FIX THIS LATER
    
    questions = models.ManyToManyField("questions.Question", related_name="quizzes", blank=True)