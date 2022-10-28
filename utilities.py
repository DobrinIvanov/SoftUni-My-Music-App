# Delete instance instead of save

# class ProfileDeleteForm(BaseProfileForm):
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.__disable_fields()
#
#     class Meta:
#         model = UserCustomModel
#         fields = ["first_name", "last_name", "age", "profile_picture"]
#
#     def save(self, commit=True):
#         if commit:
#             self.instance.delete()
#         return self.instance
#
#     def __disable_fields(self):
#         for _, field in self.fields.items():
#             field.widget.attrs["readonly"] = "disable"


# Decorator

# def return_game_obj_decor(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         pk = kwargs["pk"]
#         try:
#             game = GameModel.objects.filter(id=pk).first()
#             return func(game, *args)
#         except GameModel.DoesNotExist:
#             raise IndexError(f"Game with id-{pk} does not exist.")
#     return wrapper


# Disable fields

# class DeleteAlbumForm(AlbumBaseForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.__disable_fields()
#
#     def __disable_fields(self):
#         for _, field in self.fields.items():
#             field.widget.attrs["disabled"] = ""
