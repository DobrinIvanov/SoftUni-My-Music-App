from django.urls import path, include

from my_music_app.mymusicapp.views import add_album, index, details_album, edit_album, delete_album, details_profile, \
    delete_profile

urlpatterns = (
    path('', index, name='index'),
    path('album/', include([
        path('add/', add_album, name='add_album'),
        path('details/<int:pk>/', details_album, name='details_album'),
        path('edit/<int:pk>/', edit_album, name="edit_album"),
        path('delete/<int:pk>/', delete_album, name="delete_album")
    ])),
    path('profile/', include([
        path('details/', details_profile, name='details_profile'),
        path('delete/', delete_profile, name='delete_profile'),
    ]))
)
