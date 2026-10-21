from django.db import models
from django.utils import timezone

# Create your models here.

class Quiz(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    teacher = models.ForeignKey("users.CustomUser", on_delete=models.CASCADE) 
