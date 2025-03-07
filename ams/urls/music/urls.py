from django.urls import path

from music.views import GetSongsForArtist, CreateSongForArtist, UpdateSongForArtist, DeleteSongForArtist

urlpatterns = [
    # Music end-point
    path("list/artist/<int:artist_id>", GetSongsForArtist.as_view(), name="get-music-artist"),
    path("create", CreateSongForArtist.as_view(), name="add-music"),
    path("<int:pk>/update/artist", UpdateSongForArtist.as_view(), name="update-music"),
    path("<int:pk>/delete/artist", DeleteSongForArtist.as_view(), name="delete-music"),
]
