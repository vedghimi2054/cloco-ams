from django.db import models

from choice.gender import Gender


# Create your models here.
class Artist(models.Model):
    id = models.AutoField(primary_key=True)

    # Fields
    name = models.CharField(max_length=255, blank=True)
    dob = models.DateTimeField(null=True, blank=True)
    gender = models.IntegerField(choices=Gender,null=True, blank=True)
    address = models.CharField(max_length=255, blank=True)
    first_release_year = models.PositiveIntegerField(null=True, blank=True)
    no_of_albums_released = models.IntegerField(null=True, blank=True)

    # Auto-generated fields
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    # Meta options
    class Meta:
        db_table = 'artist'
        verbose_name = 'Artist'
        verbose_name_plural = 'Artists'