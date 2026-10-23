from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# Create your models here.
class CustomUser(AbstractUser):
    username = models.CharField(maxlength=20, unique=True, blank=False)
    email = models.EmailField(unique=True, blank=False)
    USER_TYPE_CHOICES = [
        ("STUDENT", "Student"),
        ("TEACHER", "Teacher"),
        ("ADMIN", "Admin"),
        ("SUPERUSER", "Superuser"),
    ]
    
    user_type = models.CharField(choices=USER_TYPE_CHOICES, max_length=9)