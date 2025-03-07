from rest_framework import filters
from rest_framework.generics import ListAPIView

from authentication.permission.user import IsSuperAdmin
from user.models import User
from user.serializers import ListUserSerializer


class ListUserView(ListAPIView):
    permission_classes = [IsSuperAdmin]
    queryset = User.objects.all()
    serializer_class = ListUserSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ['email']
