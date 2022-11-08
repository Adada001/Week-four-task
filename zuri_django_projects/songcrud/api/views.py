from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK,HTTP_201_CREATED,HTTP_400_BAD_REQUEST,HTTP_404_NOT_FOUND 

from .serializers import ArtisteSerializer, LyricSerializer, SongSerializer
from musicapp.models import Artiste, Song, Lyric


# Create your views here.
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def artiste_list_api(request):
    if request.method == 'GET':
        artiste = Artiste.objects.all()
        artiste_serializer = ArtisteSerializer(artiste, many=True)
        return Response(artiste_serializer.data, status=HTTP_200_OK)

    if request.method == 'POST':
        artiste_serializer = ArtisteSerializer(data=request.data)
        if artiste_serializer.is_valid():
            artiste_serializer.save()
            return Response(artiste_serializer.data, status=HTTP_201_CREATED)
        return Response(artiste_serializer.error, status=HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def artiste_api_id(request, id):
    try:
        artiste = Artiste.objects.get(id=id)
    except Song.DoesNotExist:
        return Response({"message":"Artiste not found"}, status=HTTP_400_BAD_REQUEST)
    
    if request.method == 'GET':
        artiste_serializer = ArtisteSerializer(artiste)
        return Response(artiste_serializer.data, status=HTTP_200_OK)
    if request.method == 'PUT':
        #data = JSONParser().parse(request)
        artiste_serializer = ArtisteSerializer(data=request.data)
        if artiste_serializer.is_valid():
            artiste_serializer.save()
            return Response(artiste_serializer.data, status=HTTP_201_CREATED)
        return Response(artiste_serializer.errors, status=HTTP_400_BAD_REQUEST)
    if request.method == "DELETE":
        artiste.delete()
        return Response({"message":"Artiste deleted"}, status=HTTP_404_NOT_FOUND)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def song_list_api(request):
    if request.method == 'GET':
        song = Song.objects.all()
        song_serializer = SongSerializer(song, many=True)
        return Response(song_serializer.data, status=HTTP_200_OK)

    if request.method == 'POST':
        song_serializer = SongSerializer(data=request.data)
        if song_serializer.is_valid():
            song_serializer.save()
            return Response(song_serializer.data, status=HTTP_201_CREATED)
        return Response(song_serializer.error, status=HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def song_api_id(request, id):
    try:
        song = Song.objects.get(id=id)
    except Song.DoesNotExist:
        return Response({"message":"Song not found"}, status=HTTP_400_BAD_REQUEST)
    
    if request.method == 'GET':
        song_serializer = SongSerializer(song)
        return Response(song_serializer.data, status=HTTP_200_OK)
    if request.method == 'PUT':
        #data = JSONParser().parse(request)
        song_serializer = SongSerializer(data=request.data)
        if song_serializer.is_valid():
            song_serializer.save()
            return Response(song_serializer.data, status=HTTP_201_CREATED)
        return Response(song_serializer.errors, status=HTTP_400_BAD_REQUEST)
    if request.method == "DELETE":
        song.delete()
        return Response({"message":"Song deleted"}, status=HTTP_404_NOT_FOUND)

@api_view(['GET', 'POST', 'DELETE'])
def lyric_list_api(request):
    if request.method == 'GET':
        lyric = Lyric.objects.all()
        lyric_serializer = LyricSerializer(lyric, many=True)
        return Response(lyric_serializer.data, status=HTTP_200_OK)

    if request.method == 'POST':
        lyric_serializer = LyricSerializer(data=request.data)
        if lyric_serializer.is_valid():
            lyric_serializer.save()
            return Response(lyric_serializer.data, status=HTTP_201_CREATED)
        return Response(lyric_serializer.error, status=HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def lyric_api_id(request, id):
    try:
        lyric = Lyric.objects.get(id=id)
    except Lyric.DoesNotExist:
        return Response({"message":"Lyric not found"}, status=HTTP_400_BAD_REQUEST)
    
    if request.method == 'GET':
        lyric_serializer = LyricSerializer(lyric)
        return Response(lyric_serializer.data, status=HTTP_200_OK)
    if request.method == 'PUT':
        #data = JSONParser().parse(request)
        lyric_serializer = LyricSerializer(data=request.data)
        if lyric_serializer.is_valid():
            lyric_serializer.save()
            return Response(lyric_serializer.data, status=HTTP_201_CREATED)
        return Response(lyric_serializer.errors, status=HTTP_400_BAD_REQUEST)
    if request.method == "DELETE":
        lyric.delete()
        return Response({"message":"Lyric deleted"}, status=HTTP_404_NOT_FOUND)
