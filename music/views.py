from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Album

def index(request):
    all_album = Album.objects.all()

    context = {
        'all_albums': all_album,
    }

    return render(request,'music/index.html',context)

def detail(request, aid):
    album = get_object_or_404(Album, pk=aid)
    return render(request,'music/detail.html', { 'album' : album})

def fav(request, aid):
    album = get_object_or_404(Album, pk=aid)
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except (KeyError,Song.DoesNotExist):
        return render(request,'music/detail.html',{
            'album': album,
            'error_message': 'You did not selected a song',
        })

    else:
        selected_song.is_fav = True
        selected_song.save()
        return render(request, 'music/detail.html', {'album': album})


