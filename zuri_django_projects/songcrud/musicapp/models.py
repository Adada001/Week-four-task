from email.policy import default
from django.db import models
from django.conf import settings

from unittest.util import _MAX_LENGTH
from datetime import datetime

# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    age = models.IntegerField()

    def __str__(self):
        return self.first_name

class Song(models.Model):
    title = models.CharField(max_length=40)
    release_date = models.DateTimeField(default =datetime.today)
    likes = models.PositiveIntegerField(default = 0)
    artiste_id = models.ForeignKey(Artiste, on_delete = models.CASCADE)

    def __str__(self):
        return self.title
class Lyric(models.Model):
    content = models.TextField(max_length=5000)
    song_id = models.ForeignKey(Song, on_delete = models.CASCADE)

    def __str__(self):
        return self.content

