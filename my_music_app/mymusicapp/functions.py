from my_music_app.mymusicapp.models import Profile


def get_profile():
    try:
        profile = Profile.objects.get()
        return profile
    except Profile.DoesNotExist as ex:
        return None
