from django.test import TestCase
from .models import CustomUser
from .views import UserViewSet

from rest_framework.test import APIRequestFactory
from rest_framework.reverse import reverse

class UserTestCase(TestCase):
    def setUp(self):
        self.test_user = CustomUser.objects.create_user(
            email='example_user@example.com', 
            user_type="TEACHER", 
            password='example_password'
        )
        
        self.factory = APIRequestFactory()
        self.view = UserViewSet.as_view(actions={
            'get': 'retrieve',
            'put': 'update',
            'patch': 'partial_update',
            'delete': 'destroy',
        })
        
    def test_get_user(self):
        request = self.factory.get(reverse('user-detail', args=(self.test_user.pk,)))
        response = self.view(request, pk=self.test_user.pk)
        self.assertEqual(response.status_code, 200)
        
    def test_get_all_users(self):
        response = self.client.get(reverse('user-list'), format='json')
        self.assertEqual(response.status_code, 200)
        
    def test_delete_user(self):
        request = self.factory.delete(reverse('user-detail', args=(self.test_user.pk,)))
        response = self.view(request, pk=self.test_user.pk)
        self.assertEqual(response.status_code, 204)
        
    def test_patch_user(self):
        request = self.factory.patch(
            reverse('user-detail', args=(self.test_user.pk,)),
            {'user_type': 'STUDENT'}
        )
        response = self.view(request, pk=self.test_user.pk)
        self.assertEqual(response.status_code, 200)
        
    def test_put_user(self):
        request = self.factory.put(
            reverse('user-detail', args=(self.test_user.pk,)),
            {
                'email': 'updated_user@example.com',
                'user_type': 'TEACHER',
                'password': 'new_password'
            }
        )
        response = self.view(request, pk=self.test_user.pk)
        self.assertEqual(response.status_code, 200)
        
    def test_post_user(self):
        response = self.client.post(
            reverse('user-list'), 
            {
                'email': 'new_user@example.com',
                'user_type': 'TEACHER',
                'password': 'securepassword123'
            }, 
            format='json'
        )
        
        self.assertEqual(response.status_code, 201)
        self.assertEqual(CustomUser.objects.count(), 2)
        
    def test_student_cannot_create_question(self):
        student_user = CustomUser.objects.create_user(
            email='student@example.com', 
            user_type="STUDENT", 
            password='password123'
        )
        
        self.client.force_authenticate(user=student_user)
        
        response = self.client.post(
            reverse('question-list'), 
            {
                'name': 'Student Question',
                'description': 'desc',
                'question_type': 'MCQ',
                'question': 'Sample?',
                'correct_answer': 'A',
                'incorrect_answers': ['B']
            }, 
            format='json'
        )
        
        # 401 = forbidden, 403 = unauthorized
        self.assertIn(response.status_code, [401, 403])