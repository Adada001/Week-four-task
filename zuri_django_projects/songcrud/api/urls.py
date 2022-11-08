from django.urls import path

from django.http import HttpResponse

from .views import artiste_api_id, artiste_list_api, song_api_id, song_list_api, lyric_api_id, lyric_list_api

urlpatterns = [
    path('artiste_list/', artiste_list_api, name='artiste_list_api'),
    path('artiste_list/<int:id>/', artiste_api_id, name='artiste_api_id'),
    path('song_list/', song_list_api, name='song_list_api'),
    path('song_list/<int:id>/', song_api_id, name='song_api_id'),
    path('lyric_list/', lyric_list_api, name='lyric_list_api'),
    path('lyric_list/<int:id>/', lyric_api_id, name='lyric_api_id'),

]