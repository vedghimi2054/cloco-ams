from rest_framework.generics import UpdateAPIView

from artist.models import Artist
from artist.serializers.update import UpdateArtistSerializer
from authentication.permission.artist import IsSuperAdminOrArtistManager


class UpdateArtistView(UpdateAPIView):
    permission_classes = [IsSuperAdminOrArtistManager]
    queryset = Artist.objects.all()
    serializer_class = UpdateArtistSerializer
