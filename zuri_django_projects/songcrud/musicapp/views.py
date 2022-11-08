from django.shortcuts import render
from django.http import HttpResponse
from .models import Song, Artiste, Lyric

# Create your views here.
def index(request):
    #return HttpResponse("This is my Musicapp created for week four task")
    song_list = Song.objects.all()
    context = {"songs":song_list}
    return render(request, 'musicapp/song_list.html', context)

def index(request):
    #return HttpResponse("This is my Musicapp created for week four task")
    artiste_list = Artiste.objects.all()
    context = {"artiste":artiste_list}
    return render(HttpResponse(request, 'musicapp/artiste_list.html', context))

def index(request):
    #return HttpResponse("This is my Musicapp created for week four task")
    lyric_list = Lyric.objects.all()
    context = {"lyric":lyric_list}
    return render(request, 'musicapp/lyric_list.html', context)

