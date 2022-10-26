from django.shortcuts import render

# Create your views here.


def index(request):
    context = {}
    return render(request, 'core/home-with-profile.html', context)


def add_album(request):
    context = {}
    return render(request, 'album/add-album.html', context)


def details_album(request, pk):
    context = {}
    return render(request, 'album/album-details.html', context)


def edit_album(request, pk):
    context = {}
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
