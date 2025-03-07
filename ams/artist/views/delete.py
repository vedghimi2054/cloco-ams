from rest_framework.generics import DestroyAPIView

from artist.models import Artist
from artist.serializers.delete import DeleteArtistSerializer
from authentication.permission.artist import IsSuperAdminOrArtistManager


class DeleteArtistView(DestroyAPIView):
    permission_classes = [IsSuperAdminOrArtistManager]
    queryset = Artist.objects.all()
    serializer_class = DeleteArtistSerializer
