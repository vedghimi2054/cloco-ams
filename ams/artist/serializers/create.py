from rest_framework import serializers

from choice.gender import Gender
from artist.models import Artist


class CreateArtistSerializer(serializers.ModelSerializer):
    gender = serializers.ChoiceField(Gender)

    class Meta:
        model = Artist
        fields = '__all__'
