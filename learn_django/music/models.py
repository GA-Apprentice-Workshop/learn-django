from django.core.validators import MaxLengthValidator
from django.db import models


class Song(models.Model):
    title = models.CharField(max_length=300, validators=[MaxLengthValidator])
    url = models.URLField(max_length=1000)
    artist = models.CharField(max_length=255)
