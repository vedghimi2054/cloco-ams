from rest_framework.generics import UpdateAPIView

from authentication.permission.user import IsSuperAdmin
from user.models import User
from user.serializers import UpdateUserSerializer


class UpdateUserView(UpdateAPIView):
    permission_classes = [IsSuperAdmin]
    queryset = User.objects.all()
    serializer_class = UpdateUserSerializer
