from rest_framework.generics import DestroyAPIView

from authentication.permission.music import IsArtistPermission
from music.models import Music
from music.serializers.delete import DeleteMusicSerializer


class DeleteSongForArtist(DestroyAPIView):
    permission_classes = [IsArtistPermission]
    queryset = Music.objects.all()
    serializer_class = DeleteMusicSerializer
