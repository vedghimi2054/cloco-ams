from rest_framework.generics import UpdateAPIView

from authentication.permission.music import IsArtistPermission
from music.models import Music
from music.serializers.update import UpdateMusicSerializer


class UpdateSongForArtist(UpdateAPIView):
    permission_classes = [IsArtistPermission]
    queryset = Music.objects.all()
    serializer_class = UpdateMusicSerializer
