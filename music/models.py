from django.db import models

# Create your models here.
class Album (models.Model):
    artist = models.CharField(max_length=100)
    album_title = models.CharField(max_length=100)
    genre = models.CharField(max_length=500)
    description= models.TextField(default="kaisa hai")
    time=models.DecimalField(decimal_places=2, max_digits=20)

    def __str__(self):
        return self.artist + '-' + self.album_title

class Song (models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)



