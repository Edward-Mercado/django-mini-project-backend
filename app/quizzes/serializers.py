from .models import Quiz
from rest_framework import serializers

class QuizSerializer(serializers.HyperlinkedModelSerializer):
    teacher = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Quiz
        fields = ['id', 'name', 'teacher', 'questions']