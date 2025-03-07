# Create your views here.

from rest_framework import status
from rest_framework.generics import UpdateAPIView, CreateAPIView, DestroyAPIView, ListAPIView, get_object_or_404, \
    RetrieveAPIView
from rest_framework.response import Response

from artist.models import Artist
from core.constant import ARTIST_NOT_FOUND_ERROR, MUSIC_NOT_FOUND_ERROR
from music.models import Music
from base.pagination.pagination import CustomPagination
from music.serializers import MusicSerializer


class CreateSongForArtist(CreateAPIView):
    def post(self, request, *args, **kwargs):
        artist_id = kwargs.get('artistId')
        try:
            artist = Artist.objects.get(id=artist_id)
        except Artist.DoesNotExist:
            return Response(ARTIST_NOT_FOUND_ERROR, status=status.HTTP_404_NOT_FOUND)
        serializer = MusicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['artist'] = artist
            serializer.save()
            return Response({"result": serializer.data})
        return Response(serializer.errors)


class UpdateSongForArtist(UpdateAPIView):
    def put(self, request, *args, **kwargs):
        try:
            artist_id = kwargs.get("artistId")
            music_id = kwargs.get("id")
            artist = Artist.objects.get(id=artist_id)
            try:
                music = Music.objects.get(id=music_id, artist=artist)
            except Music.DoesNotExist:
                return Response(MUSIC_NOT_FOUND_ERROR, status=status.HTTP_404_NOT_FOUND)
        except Artist.DoesNotExist:
            return Response(ARTIST_NOT_FOUND_ERROR, status=status.HTTP_404_NOT_FOUND)

        serializer = MusicSerializer(music, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Music updated successfully", "result": serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteSongForArtist(DestroyAPIView):
    def delete(self, request, *args, **kwargs):
        artist_id = kwargs.get("artistId")
        music_id = kwargs.get("id")
        try:
            artist = Artist.objects.get(id=artist_id)
            music = Music.objects.get(id=music_id, artist=artist)
        except Artist.DoesNotExist:
            return Response(ARTIST_NOT_FOUND_ERROR, status=status.HTTP_404_NOT_FOUND)
        except Music.DoesNotExist:
            return Response(MUSIC_NOT_FOUND_ERROR, status=status.HTTP_404_NOT_FOUND)
        music.delete()
        return Response({"message": "Music deleted successfully"})


class GetSongsForArtist(ListAPIView):
    pagination_class = CustomPagination

    def get(self, request, *args, **kwargs):
        artist_id = kwargs.get("artistId")
        artist = get_object_or_404(Artist, id=artist_id)
        songs = artist.music_set.all()
        # Use pagination to handle the query
        paginator = self.pagination_class()
        paginated_songs = paginator.paginate_queryset(songs, request)

        # Serialize the data and return it with pagination information
        serializer = MusicSerializer(paginated_songs, many=True)
        return paginator.get_paginated_response(serializer.data)
