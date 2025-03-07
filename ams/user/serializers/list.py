from rest_framework import serializers

from user.models import User


class ListUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'dob', 'address', 'gender', 'role')
