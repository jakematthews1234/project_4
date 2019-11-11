from django.db import models
from django.utils import timezone
from user.models import User


class Artwork(models.Model):
    """ The Model for Artwork, allowing the options to display it as sold, or for sale"""
    SOLD = 'sold'
    FOR_SALE = 'for sale'
    ARTWORK_STATUS_CHOICES = (
        (
            SOLD, 'sold'
        ),
        (
            FOR_SALE, 'for sale'
        )
    )
    """ The fields used to create an in depth description for each piece of Artwork. """
    picture = models.CharField(max_length=400)
    title = models.CharField(max_length=50)
    description = models.TextField()
    date_created = models.DateTimeField(default= timezone.now)
    status = models.CharField(max_length=8, choices=ARTWORK_STATUS_CHOICES, default=FOR_SALE)
    likes = models.ManyToManyField(User, through='Like', related_name='Liker')

    def __str__(self):
        return self.title


class Like(models.Model):
    """ When both user or artwork are deleted from the database, delete the Likes the artwork
    or the user has added. """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE)

    """ Linking the artwork and user together """
    class Meta:
        unique_together = ('artwork', 'user')


class Comment(models.Model):
    """ The fields used to create a way for users to comment on artwork, leaving their unique
    user id and date created along with the comment """
    artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_commented = models.DateTimeField(default=timezone.now)
    comment = models.CharField(max_length=500, blank=False)
