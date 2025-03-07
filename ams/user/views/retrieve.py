from rest_framework.generics import RetrieveAPIView

from authentication.permission.user import IsSuperAdmin
from user.models import User
from user.serializers import RetrieveUserSerializer


class RetrieveUserView(RetrieveAPIView):
    permission_classes = [IsSuperAdmin]
    queryset = User.objects.all()
    serializer_class = RetrieveUserSerializer
