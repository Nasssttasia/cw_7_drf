from django.contrib.auth.hashers import make_password
from rest_framework.serializers import ModelSerializer

from users.models import User


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

    def validate_password(self, value):
        return make_password(value)