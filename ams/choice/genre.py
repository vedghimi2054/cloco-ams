from django.db import models


class Genre(models.IntegerChoices):
    GENRE_UNSPECIFIED=0,"unspecified"
    MB= 1,"mb"
    COUNTRY=2,"country"
    CLASSIC=3,"classic"
    ROCK=4,"rock"
    JAZZ=5,"jazz"
