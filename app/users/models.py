from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, blank=False)
    USER_TYPE_CHOICES = [
        (0, "Student"),
        (1, "Teacher"),
        (2, "Admin"),
        (3, "Superuser"),
    ]
    
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)