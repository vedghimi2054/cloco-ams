from rest_framework.generics import DestroyAPIView

from authentication.permission.user import IsSuperAdmin
from user.models import User
from user.serializers import DeleteUserSerializer


class DeleteUserView(DestroyAPIView):
    permission_classes = [IsSuperAdmin]
    queryset = User.objects.all()
    serializer_class = DeleteUserSerializer
