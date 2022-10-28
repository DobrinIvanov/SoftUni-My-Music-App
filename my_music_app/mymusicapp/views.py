from django.shortcuts import render, redirect

from my_music_app.mymusicapp.forms import AddProfileForm, AlbumBaseForm, DeleteAlbumForm
from my_music_app.mymusicapp.functions import get_profile
from my_music_app.mymusicapp.models import Album, Profile


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
        album_form = AlbumBaseForm()
    else:
        album_form = AlbumBaseForm(request.POST)
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
        create_album_form = AlbumBaseForm(instance=album)
    else:
        create_album_form = AlbumBaseForm(request.POST, instance=album)
        if create_album_form.is_valid():
            create_album_form.save()
            return redirect('index')

    context = {
        'form': create_album_form,
        'album': album,
    }

    return render(request, 'album/edit-album.html', context)

# To make fields Disable in ModelForm
# def init(self, args, **kwargs):
#     super().init(args, **kwargs)
#     self.__disable_fields()
#
#
# def __disablefields(self):
#     for , field in self.fields.items():
#         field.widget.attrs["readonly"] = "disable"


def delete_album(request, pk):
    album = Album.objects.filter(pk=pk).get()
    if request.method == 'POST':
        album.delete()
        return redirect('index')
    form = DeleteAlbumForm(instance=album)
    context = {
        'form': form,
        'pk': pk,
    }
    return render(request, 'album/delete-album.html', context)


def details_profile(request):
    profile = Profile.objects.get()
    albums_count = Album.objects.all().count()
    context = {
        'profile': profile,
        'count': albums_count,
    }
    return render(request, 'profile/profile-details.html', context)


def delete_profile(request):
    if request.method == 'POST':
        Profile.objects.get().delete()
        return redirect('index')
    context = {}
    return render(request, 'profile/profile-delete.html', context)


