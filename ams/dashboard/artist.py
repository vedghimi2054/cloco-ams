from rest_framework import serializers
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from artist.models import Artist


class ArtistCountSerializer(serializers.Serializer):
    total_artists = serializers.IntegerField()


class ArtistCountView(GenericAPIView):
    serializer_class = ArtistCountSerializer

    def get(self, request, *args, **kwargs):
        total_artists = Artist.objects.count()
        return Response(self.get_serializer({'total_artists': total_artists}).data)
