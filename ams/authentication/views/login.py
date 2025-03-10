# Implement custom logic here for views.
# SimpleJWT authentication only returns the refresh and access tokens.
# If we need user information as well, we need to implement additional logic.
from rest_framework_simplejwt.views import TokenObtainPairView

from authentication.serializers import CustomTokenObtainPairSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
