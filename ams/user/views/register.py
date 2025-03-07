from rest_framework.generics import CreateAPIView

from user.models import User
from user.serializers import RegisterUserSerializer


class RegisterUser(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer
