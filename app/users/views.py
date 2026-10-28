from .models import CustomUser
from rest_framework import  viewsets, generics # Levina LM uses generics.GenericAPIView, idk why
from rest_framework.permissions import AllowAny

from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
    permission_classes = [AllowAny]