from django.core import validators
from django.db import models

from my_music_app.mymusicapp.validators import validate_username_chars

# Create your models here.


class Profile(models.Model):

    MAX_LEN_USERNAME = 15
    MIN_LEN_USERNAME = 2

    username = models.CharField(
        max_length=MAX_LEN_USERNAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_USERNAME),
            validate_username_chars,
        ),
        null=False,
        blank=False,
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.PositiveIntegerField(
        null=False,
        blank=True,
    )


class Album(models.Model):

    MAX_LEN_NAME = 30
    MAX_LEN_ARTIST = 30
    MAX_LEN_GENRE = 30

    GENRES = [
        ('Pop', 'Pop Music'),
        ('Jazz', 'Jazz Music'),
        ('R&B', 'R&B Music'),
        ('Rock', 'Rock Music'),
        ('Country', 'Country Music'),
        ('Dance Music', 'Dance Music'),
        ('Hip Hop', 'Hip Hop Music'),
        ('Other genres', 'Other'),
    ]

    name = models.CharField(
        unique=True,
        max_length=MAX_LEN_NAME,
        null=False,
        blank=False,
        verbose_name='Album Name'
    )

    artist = models.CharField(
        max_length=MAX_LEN_ARTIST,
        blank=False,
        null=False,
    )

    genre = models.CharField(
        max_length=MAX_LEN_GENRE,
        choices=GENRES,
        blank=False,
        null=False,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    image_url = models.URLField(
        blank=False,
        null=False,
        verbose_name='Image URL'
    )

    price = models.FloatField(
        validators=(validators.MinValueValidator(0),),
    )
