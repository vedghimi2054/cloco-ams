from music.serializers.create import CreateMusicSerializer
from music.serializers.update import UpdateMusicSerializer
from music.serializers.delete import DeleteMusicSerializer
from music.serializers.list import ListMusicSerializer
from artist.serializers import ListArtistSerializer

__all__ = [
    "CreateMusicSerializer",
    "UpdateMusicSerializer",
    "DeleteMusicSerializer",
    "ListMusicSerializer",
    "ListArtistSerializer",

]
