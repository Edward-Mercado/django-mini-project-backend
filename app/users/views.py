from .models import CustomUser
from rest_framework import  viewsets, generics # Levina LM uses generics.GenericAPIView, idk why
from rest_framework import permissions, viewsets

from .serializers import UserSerializer, RegisterSerializer

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all().order_by("id")
    permission_classes = [permissions.IsAuthenticated]
    # make some way for the permissions to be split in routes
    
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]