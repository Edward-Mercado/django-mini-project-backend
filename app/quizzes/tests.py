from django.test import TestCase
from django.urls import reverse

from quizzes.models import Quiz
from questions.models import Question
from users.models import CustomUser

from rest_framework.test import APIRequestFactory, APIClient, force_authenticate
from quizzes.views import QuizViewSet

# REWRITE ENTIRETY OF THIS TONIGHT

class QuizTestCase(TestCase):
    def setUp(self):
        self.test_user = CustomUser.objects.create_user(
            username="example_user",
            email="example_user@example.com",
            user_type="TEACHER",
            password="example_password",
        )

        self.test_quiz = Quiz.objects.create(
            name="TestQuiz",
            teacher=self.test_user,
        )

        self.test_question = Question.objects.create(
            name="Test Question",
            question="What is 2 + 2?",
            question_type="MCQ",
            correct_answer="4",
            incorrect_answers=["1", "2", "3"],
        )

        self.test_quiz.questions.add(self.test_question)

        self.factory = APIRequestFactory()
        self.client = APIClient()

        self.view = QuizViewSet.as_view(
            actions={
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        )

    def test_get_quiz(self):
        request = self.factory.get(reverse('quizzes-detail', args=(self.test_quiz.pk,)))
        force_authenticate(request, user=self.test_user)
        response = self.view(request, pk=self.test_quiz.pk)
        self.assertEqual(response.status_code, 200)
    
    def test_get_all_quiz(self):
        self.client.force_authenticate(user=self.test_user)
        response = self.client.get(reverse('quizzes-list'), format='json')
        self.assertEqual(response.status_code, 200)

    def test_delete_quiz(self):
        request = self.factory.delete(reverse('quizzes-detail', args=(self.test_quiz.pk,)))
        force_authenticate(request, user=self.test_user)
        response = self.view(request, pk=self.test_quiz.pk)
        self.assertEqual(response.status_code, 204)

    def test_patch_quiz(self):
        request = self.factory.patch(
            reverse('quizzes-detail', args=(self.test_quiz.pk,)),
            {'name': 'Updated Quiz Name'},    
            format='json'
        )
        force_authenticate(request, user=self.test_user)
        response = self.view(request, pk=self.test_quiz.pk)
        self.assertEqual(response.status_code, 200)
        
    def test_put_quiz(self):
        request = self.factory.put(
            reverse('quizzes-detail', args=(self.test_quiz.pk,)),
            {
                "name": "TestQuiz",
                "teacher": self.test_user.pk,
                'questions': []
            },
            format='json'
        )
        force_authenticate(request, user=self.test_user)
        response = self.view(request, pk=self.test_quiz.pk)
        self.assertEqual(response.status_code, 200)
        
    def test_post_quiz(self):
        self.client.force_authenticate(user=self.test_user)

        response = self.client.post(
            reverse('quizzes-list'),
            {
                'name': 'new quiz test',
                'questions': []
            },
            format='json'
        )

        self.assertEqual(response.status_code, 201, response.data)

        new_quiz = Quiz.objects.get(name='new quiz test')
        self.assertEqual(new_quiz.teacher, self.test_user)