from rest_framework.permissions import BasePermission

from artist.models import Artist
from choice.role import Role


class IsSuperAdminOrArtistManager(BasePermission):
    """
       Custom permission to only allow access to super_admin or artist_manager roles.
       """

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        # Check if the user has either SUPER_ADMIN or ARTIST_MANAGER role
        return request.user.role in [Role.SUPER_ADMIN, Role.ARTIST_MANAGER]

    def has_object_permission(self, request, view, obj):
        # For instance, ensure that the logged-in user is the artist owner or an admin
        if isinstance(obj, Artist):
            # Only allow delete if the user is a super_admin or artist_manager
            return request.user.role == Role.SUPER_ADMIN or request.user.role == Role.ARTIST_MANAGER
        return False
