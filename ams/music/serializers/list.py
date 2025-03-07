from rest_framework import serializers

from artist.serializers import ListArtistSerializer
from choice.genre import Genre
from music.models import Music


class ListMusicSerializer(serializers.ModelSerializer):
    genre = serializers.ChoiceField(Genre)
    artist = ListArtistSerializer()

    class Meta:
        model = Music
        fields = ['id', 'title', 'album_name', 'genre', 'artist']
