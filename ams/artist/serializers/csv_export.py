from rest_framework import serializers

from artist.models import Artist


class ArtistExportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('id', 'name', 'dob', 'gender', 'address', 'first_release_year', 'no_of_albums_released')
