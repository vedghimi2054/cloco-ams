from rest_framework import serializers
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from user.models import User


class UserCountSerializer(serializers.Serializer):
    total_users = serializers.IntegerField()


class UserCountView(GenericAPIView):
    serializer_class = UserCountSerializer

    def get(self, request, *args, **kwargs):
        total_users = User.objects.count()
        return Response(self.get_serializer({'total_users': total_users}).data)