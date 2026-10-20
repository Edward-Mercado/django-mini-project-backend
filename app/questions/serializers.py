from .models import Question
from rest_framework import serializers

class QuestionSerializer:
    class Meta:
            model = Question
            fields = ['question_type', 'description', 'question', 'correct_answer', 'incorrect_answers', 'quizzes']