from rest_framework.permissions import AllowAny

from users.serializers import UserSerializer
from rest_framework import generics


# Create your views here.
class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]