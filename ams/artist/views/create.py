from rest_framework.generics import CreateAPIView

from artist.models import Artist
from artist.serializers.create import CreateArtistSerializer
from authentication.permission.artist import IsSuperAdminOrArtistManager


class SaveArtistView(CreateAPIView):
    permission_classes = [IsSuperAdminOrArtistManager]
    queryset = Artist.objects.all()
    serializer_class = CreateArtistSerializer
