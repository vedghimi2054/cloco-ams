from rest_framework.generics import ListAPIView

from artist.models import Artist
from artist.serializers.list import ListArtistSerializer
from authentication.permission.artist import IsSuperAdminOrArtistManager
from base.pagination.pagination import CustomPagination


class GetAllArtistsView(ListAPIView):
    permission_classes = [IsSuperAdminOrArtistManager]
    queryset = Artist.objects.all()
    serializer_class = ListArtistSerializer
    pagination_class = CustomPagination
