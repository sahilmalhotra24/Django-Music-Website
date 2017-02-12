from django.db import models

class Album(models.Model):
    artist = models.CharField(max_length=500)
    album_title = models.CharField(max_length=250)
    genere = models.CharField(max_length=100)
    logo = models.CharField(max_length=100)

    def __str__(self):
        return self.album_title + ' - ' +self.artist

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=100)
    is_fav = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title

# Create your models here.1
