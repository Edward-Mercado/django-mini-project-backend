from .models import Quiz
from rest_framework import serializers

# serializers convert data from other languages into python objects and vice versa
# remember this is used as an api
        
class QuizSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Quiz,
        fields = ['id', 'name', 'teacher', 'questions']