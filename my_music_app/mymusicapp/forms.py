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


class AlbumBaseForm(forms.ModelForm):
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


class EditAlbumForm(AlbumBaseForm):
    pass


class DeleteAlbumForm(AlbumBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__disable_fields()

    def __disable_fields(self):
        for _, field in self.fields.items():
            field.widget.attrs["disabled"] = ""
            # field.required = False

    def __disable_select_field(self):
        pass


# class DeleteProfileForm(forms.Form):
#     pass
