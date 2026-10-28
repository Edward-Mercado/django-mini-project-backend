from django.test import TestCase
from users.models import CustomUser
from .models import Question
from quizzes.models import Quiz
from .views import QuestionViewSet

from rest_framework.test import APIRequestFactory
from rest_framework.reverse import reverse

class QuestionTestCase(TestCase):
    def setUp(self):
        self.test_question = Question.objects.create(
            name="TestQuestion", 
            description="sample desc",
            question_type="MCQ",
            question="How to test???",
            correct_answer="in tests.py",
            incorrect_answers=["don't", "just wing it", "vibecode"],
            ) # many to many fields are not defined here
        
        sample_user = CustomUser.objects.create(
            email='example_user@example.com', 
            user_type="TEACHER", 
            password='example_password'
        )
        
        quiz1 = Quiz.objects.create(name='edward quiz', teacher=sample_user)
        
        self.test_question.quizzes.set([quiz1]) # define here
        
        self.factory = APIRequestFactory()
        self.view = QuestionViewSet.as_view(actions={
            'get': 'retrieve',
            'put': 'update',
            'patch': 'partial_update',
            'delete': 'destroy',
        })
        
    def test_get_question(self):
        request = self.factory.get(reverse('question-detail', args=(self.test_question.pk,)))
        response = self.view(request)
        self.assertEqual(response.status_code, 200)
        
    def test_get_all_question(self):
        response = self.client.get(reverse('question-list'), {'name': 'Basic Test Question'}, format='json')
        self.assertEqual(response.status_code, 200)
        
    def test_delete_question(self):
        request = self.factory.delete(reverse('question-detail', args=(self.test_question.pk,)))
        response = self.view(request)
        self.assertEqual(response.status_code, 204)
        
    def test_patch_question(self):
        request = self.factory.patch(reverse('question-detail', args=(self.test_question.pk,)))
        response = self.view(request)
        self.assertEqual(response.status_code, 200)
        
    def test_put_question(self):
        request = self.factory.put(reverse('question-detail', args=(self.test_question.pk,)))
        response = self.view(request)
        self.assertEqual(response.status_code, 200)
        
    def test_post_question(self):
        response = self.client.post(reverse('question-list'), {'name': 'Basic Test Question'}, format='json')
        new_question = Question.objects.get(name="Basic Test Question")
        
        
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Question.objects.count(), 2)
        self.assertEqual(Question.objects.get().name, "Basic Test Question") 
        self.assertEqual(new_question.name, "Basic Test Quiz")