from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from artist.models import Artist


class ArtistCountView(GenericAPIView):
    def get(self, request, *args, **kwargs):
        total_artists = Artist.objects.count()
        return Response({'total_artists': total_artists})
