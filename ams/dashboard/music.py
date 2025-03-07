from rest_framework import serializers
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from music.models import Music


class MusicCountSerializer(serializers.Serializer):
    total_music = serializers.IntegerField()


class MusicCountView(GenericAPIView):
    serializer_class = MusicCountSerializer

    def get(self, request, *args, **kwargs):
        total_music = Music.objects.count()
        return Response(self.get_serializer({'total_music': total_music}).data)
