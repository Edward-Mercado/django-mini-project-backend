from django.test import TestCase

# Create your tests here.

from quizzes.models import Quiz
from users.models import CustomUser
from quizzes.views import QuizViewSet
from rest_framework.test import APIRequestFactory
from rest_framework.reverse import reverse

class QuizTestCase(TestCase):
    def setUp(self):
        sample_user = CustomUser.objects.create(
            email='example_user@example.com', 
            user_type="TEACHER", 
            password='example_password'
        )
        self.test_quiz = Quiz.objects.create(name="TestQuiz", teacher=sample_user) 
        self.factory = APIRequestFactory()
        self.view = QuizViewSet.as_view(actions={
            'get': 'retrieve',
            'put': 'update',
            'patch': 'partial_update',
            'delete': 'destroy',
        })

        # creates a sample object
        
    def test_get_quiz(self):
        request = self.factory.get(reverse('quiz-detail', args=(self.test_quiz.pk,)))
        # creates an HTTP request
        response = self.view(request)
        # runs the request
        self.assertEqual(response.status_code, 200)
        # assertEqual(expected, actual) ensures that your actual outcome is the same as expected
        # 200 is "good, data returned"
        
    def test_get_all_quiz(self):
        response = self.client.get(reverse('quiz-list'), {'name': 'Basic Test Quiz'}, format='json')
        self.assertEqual(response.status_code, 200)
        
    def test_delete_quiz(self):
        request = self.factory.delete(reverse('quiz-detail', args=(self.test_quiz.pk,)))
        response = self.view(request)
        self.assertEqual(response.status_code, 204)
        # 204 means "good, no data to send back" (because we deleted it)
        
    def test_patch_quiz(self):
        request = self.factory.patch(reverse('quiz-detail', args=(self.test_quiz.pk,)))
        response = self.view(request)
        self.assertEqual(response.status_code, 200)
        
    def test_put_quiz(self):
        request = self.factory.put(reverse('quiz-detail', args=(self.test_quiz.pk,)))
        response = self.view(request)
        self.assertEqual(response.status_code, 200)
        
    def test_post_quiz(self):
        response = self.client.post(reverse('quiz-list'), {'name': 'Basic Test Quiz'}, format='json')
        # different syntax for sample post
        self.assertEqual(response.status_code, 201)
        # 201 means "good, more data added"
        self.assertEqual(Quiz.objects.count(), 2)
        self.assertEqual(Quiz.objects.get().name, "Basic Test Quiz")
        
        new_quiz = Quiz.objects.get(name="Basic Test Quiz")
        self.assertEqual(new_quiz.name, "Basic Test Quiz")