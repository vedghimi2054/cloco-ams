from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from artist.models import Artist
from music.models import Music
from user.models import User


class DashboardCountView(ListAPIView):
    def get(self, request, *args, **kwargs):
        total_artists = Artist.objects.count()
        total_users = User.objects.count()
        total_music = Music.objects.count()

        return Response({'total_artists': total_artists, 'total_users': total_users, 'total_music': total_music})
