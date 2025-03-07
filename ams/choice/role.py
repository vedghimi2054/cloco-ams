from django.db import models


class Role(models.IntegerChoices):
    ROLE_UNSPECIFIED = 0, 'Unspecified'
    SUPER_ADMIN = 1, 'Super Admin'
    ARTIST_MANAGER = 2, 'Artist Manager'
    ARTIST = 3, 'Artist'
