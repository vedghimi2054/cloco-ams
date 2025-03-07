from django.db import models


class Gender(models.IntegerChoices):
    GENDER_UNSPECIFIED = 0,"unspecified"
    MALE = 1, "male"
    FEMALE = 2,  "female"
    OTHER = 3,"other"
