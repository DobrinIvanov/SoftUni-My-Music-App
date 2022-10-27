from django import forms

from my_music_app.mymusicapp.models import Profile, Album


class AddProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'},),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'},),
            'age': forms.NumberInput(attrs={'placeholder': 'Age'},),
        }


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Album Name'},),
            'artist': forms.TextInput(attrs={'placeholder': 'Artist'},),
            # 'genre': forms.Select(choices=Album.GENRES),
            'description': forms.Textarea(attrs={'placeholder': 'Description'}, ),
            'image_url': forms.TextInput(attrs={'placeholder': 'Image URL'}, ),
            'price': forms.NumberInput(attrs={'placeholder': 'Price', }, ),
        }

# class EditAlbumForm(forms.ModelForm):
#     class Meta:
#         model = Album
#         fields = '__all__'

