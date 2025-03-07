from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from music.models import Music


class MusicCountView(GenericAPIView):
    def get(self, request, *args, **kwargs):
        total_music = Music.objects.count()
        return Response({'total_music': total_music})
