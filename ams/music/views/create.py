from rest_framework.generics import CreateAPIView

from authentication.permission.music import IsArtistPermission
from music.models import Music
from music.serializers.create import CreateMusicSerializer


class CreateSongForArtist(CreateAPIView):
    permission_classes = [IsArtistPermission]
    queryset = Music.objects.all()
    serializer_class = CreateMusicSerializer
