from .models import Question
from rest_framework import serializers

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
            model = Question
            fields = ['name', 'id', 'question_type', 'description', 'question', 'correct_answer', 'incorrect_answers', 'quizzes']