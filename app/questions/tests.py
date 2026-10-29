from django.test import TestCase
from users.models import CustomUser
from .models import Question
from quizzes.models import Quiz
from .views import QuestionViewSet

from rest_framework.test import APIRequestFactory, force_authenticate, APIClient
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
        
        self.sample_user = CustomUser.objects.create_user(
            username='example_user',
            email='example_user@example.com', 
            user_type="TEACHER", 
            password='example_password',
        )
        
        quiz1 = Quiz.objects.create(name='edward quiz', teacher=self.sample_user)
        
        self.test_question.quizzes.set([quiz1]) # define here
        self.client = APIClient()
        
        self.factory = APIRequestFactory()
        self.view = QuestionViewSet.as_view(actions={
            'get': 'retrieve',
            'put': 'update',
            'patch': 'partial_update',
            'delete': 'destroy',
        })
        
    def test_get_question(self):
        request = self.factory.get(reverse('question-detail', args=(self.test_question.pk,)))
        force_authenticate(request, user=self.sample_user)
        response = self.view(request, pk=self.test_question.pk)
        self.assertEqual(response.status_code, 200)
        
    def test_get_all_question(self):
        self.client.force_authenticate(user=self.sample_user)
        response = self.client.get(reverse('question-list'), format='json')
        self.assertEqual(response.status_code, 200)
        
    def test_delete_question(self):
        request = self.factory.delete(reverse('question-detail', args=(self.test_question.pk,)))
        force_authenticate(request, user=self.sample_user)
        response = self.view(request, pk=self.test_question.pk)
        self.assertEqual(response.status_code, 204)
        
    def test_patch_question(self):
        request = self.factory.patch(
            reverse('question-detail', args=(self.test_question.pk,)),
            {'name': 'Updated Question'},
            format='json'
        )
        force_authenticate(request, user=self.sample_user)
        response = self.view(request, pk=self.test_question.pk)

        self.assertEqual(response.status_code, 200)
        
    def test_put_question(self):
        request = self.factory.put(
            reverse('question-detail', args=(self.test_question.pk,)),
            {
                'name': 'Updated Question',
                'description': 'Updated description',
                'question_type': 'MCQ',
                'question': 'What is 2 + 2?',
                'correct_answer': '4',
                'incorrect_answers': ['3', '5', '6'],
            },
            format='json'
        )
        force_authenticate(request, user=self.sample_user)
        response = self.view(request, pk=self.test_question.pk)

        self.assertEqual(response.status_code, 200)
        
    def test_post_question(self):
        self.client.force_authenticate(user=self.sample_user)
        response = self.client.post(
            reverse('question-list'),
            {
                'name': 'Basic Test Question',
                'description': 'sample desc',
                'question_type': 'MCQ',
                'question': 'How to test???',
                'correct_answer': 'in tests.py',
                'incorrect_answers': ["don't", "just wing it", "vibecode"],
            },
            format='json'
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(Question.objects.count(), 2)

        new_question = Question.objects.get(name='Basic Test Question')
        self.assertEqual(new_question.name, 'Basic Test Question')