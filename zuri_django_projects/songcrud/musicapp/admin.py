from django.contrib import admin
from .models import Artiste, Song, Lyric
# Register your models here.

admin.site.register(Artiste)
admin.site.register(Song)
admin.site.register(Lyric)

class Artiste_admin (admin.ModelAdmin):
    artiste_details =['first_name','last_name','age']

class Song_admin (admin.ModelAdmin):
    song_details =['titel', 'release_date', 'likes', 'artiste_id']

class Lyric_admin (admin.ModelAdmin):
    lyric_details =['content', 'song_id']