from django.shortcuts import render, redirect

from my_music_app.mymusicapp.forms import AddProfileForm, AlbumForm
from my_music_app.mymusicapp.functions import get_profile
from my_music_app.mymusicapp.models import Album


# Create your views here.


def index(request):
    profile = get_profile()
    if profile is None:
        return add_profile(request)
    albums = Album.objects.all()
    context = {
        'profile': profile,
        'albums': albums,
    }
    return render(request, 'core/home-with-profile.html', context)


def add_profile(request):
    if request.method == "GET":
        form = AddProfileForm()
    else:
        form = AddProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'profile': False,
        'form': form,
    }
    return render(
        request,
        'core/home-no-profile.html',
        context,
    )


def add_album(request):
    if request.method == "GET":
        album_form = AlbumForm()
    else:
        album_form = AlbumForm(request.POST)
        if album_form.is_valid():
            album_form.save()
            return redirect('index')
    context = {
        'album_form': album_form,
    }
    return render(request, 'album/add-album.html', context)


def details_album(request, pk):
    album = Album.objects.get(pk=pk)
    context = {
        'album': album,
    }
    return render(request, 'album/album-details.html', context)


def edit_album(request, pk):

    album = Album.objects.get(pk=pk)

    if request.method == 'GET':
        create_album_form = AlbumForm(instance=album)
    else:
        create_album_form = AlbumForm(request.POST, instance=album)
        if create_album_form.is_valid():
            create_album_form.save()
            return redirect('index')

    context = {
        'form': create_album_form,
        'album': album,
    }

    return render(request, 'album/edit-album.html', context)


def delete_album(request, pk):
    context = {}
    return render(request, 'album/delete-album.html', context)


def details_profile(request):
    context = {}
    return render(request, 'profile/profile-details.html', context)


def delete_profile(request):
    context = {}
    return render(request, 'profile/profile-delete.html', context)


