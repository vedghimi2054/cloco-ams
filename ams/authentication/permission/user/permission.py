from rest_framework.permissions import BasePermission

from choice.role import Role
from user.models import User


class IsSuperAdmin(BasePermission):
    """
       Custom permission to only allow access to super_admin.
       """

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        # Check if the user has either SUPER_ADMIN or ARTIST_MANAGER role
        return request.user.role == Role.SUPER_ADMIN

    def has_object_permission(self, request, view, obj):
        # For instance, ensure that the logged-in user is super_admin
        if isinstance(obj, User):
            # Only allow if the user is a super_admin
            return request.user.role == Role.SUPER_ADMIN
        return False
