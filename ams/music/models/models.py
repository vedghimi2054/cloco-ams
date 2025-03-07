# Create your models here.
from django.db import models

from choice.genre import Genre


class Music(models.Model):
    artist = models.ForeignKey('artist.Artist', on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=255, blank=True)
    album_name = models.CharField(max_length=255, blank=True)
    genre = models.IntegerField(choices=Genre,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.title or 'Untitled Music'

    class Meta:
        db_table = 'music'
