from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied

from choice.role import Role
from user.models import User


class UpdateUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'phone', 'address', 'dob', 'gender', 'role', 'password')

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        if password:
            instance.set_password(password)

        # Handle role assignment: Only super admins can update the role
        if 'role' in validated_data:
            if self.context['request'].user.role != Role.SUPER_ADMIN:
                raise PermissionDenied("You do not have permission to update the role.")
            instance.role = validated_data['role']

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
