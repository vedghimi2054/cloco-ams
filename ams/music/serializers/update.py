from rest_framework import serializers

from choice.genre import Genre
from music.models import Music


class UpdateMusicSerializer(serializers.ModelSerializer):
    genre = serializers.ChoiceField(Genre)

    class Meta:
        model = Music
        fields = ['id','title', 'album_name', 'genre', 'artist']
