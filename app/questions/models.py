from django.db import models

# Create your models here.

class Question(models.Model):
    QUESTION_TYPES = [
        ("FRQ", "Free Response Question"),
        ("MCQ", "Multiple Choice Question"),
    ]
    name = models.CharField(max_length=100)
    
    description = models.TextField(null=True, blank=True) 
    # description is nullable, and the validation forms can accept it as blank
    
    question_type = models.CharField(max_length=3, choices=QUESTION_TYPES) 
    # question_type is an enum type
    
    question = models.TextField(null=False, blank=False) 
    correct_answer = models.TextField(null=False, blank=False)
    incorrect_answers = models.JSONField(default=list, blank=True)
    # allows multiple incorrect answers, but one correct answer, the latter being required
    
    quizzes = models.ManyToManyField("quizzes.Quiz", related_name="questions", blank=True)
    # this question can be a part of many quizzes, and it can be linked through the questions property of the quiz