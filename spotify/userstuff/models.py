from django.db import models
from django.conf import settings
from django.urls import reverse
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=100)
    #public_playlist = models.ManyToManyField(Song, null=True, blank=True, on_delete=models.CASCADE, related_name="public_playlist")
    profile_image = models.ImageField(null=True, blank=True, upload_to="images/profile_pic/")

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE, related_name="user_profile")
    public_playlist = models.ManyToManyField("Song",  related_name="public_playlist")
    followers = models.ManyToManyField('self', blank=True, related_name='user_followers', symmetrical=False)
    following = models.ManyToManyField('self', blank=True, related_name='user_following', symmetrical=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['followers', 'following'], name='follow-stuff')
        ]

    def __str__(self):
        return '%s' % (self.user)

# class UserFollowing(models.Model):
#     user_id = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE, related_name="following")




    # You can even add info about when user started following
    # created = models.DateTimeField(auto_now_add=True)



class Song(models.Model):
    song_name = models.CharField(max_length=100)
    song_file = models.FileField(blank=True, null=True, upload_to="songs/")
    song_link = models.CharField(max_length=200, blank=True, null=True)
    song_pic = models.ImageField(upload_to="images/song_pic/")
    #songs_artist = models.OneToOneField(Artist, on_delete=models.CASCADE)
    #album_name = models.OneToOneField(Album, on_delete=models.CASCADE)

    def __str__(self):
        return self.song_name

    def get_absolute_url(self):
        return reverse('general:home')
