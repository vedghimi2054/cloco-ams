from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.permissions import AllowAny

from artist.models import Artist
from base.pagination.pagination import CustomPagination
from music.models import Music
from music.serializers.list import ListMusicSerializer


class GetSongsForArtist(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = ListMusicSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        artist_id = self.kwargs.get('artist_id')
        artist = get_object_or_404(Artist, id=artist_id)
        return Music.objects.filter(artist=artist)
