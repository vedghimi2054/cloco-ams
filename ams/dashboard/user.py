from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from user.models import User


class UserCountView(GenericAPIView):
    def get(self, request, *args, **kwargs):
        total_users = User.objects.count()
        return Response({'total_users': total_users})
