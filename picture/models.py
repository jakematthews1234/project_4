from django.db import models
from django.utils import timezone
from user.models import User


class Artwork(models.Model):
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
    picture = models.CharField(max_length=400)
    title = models.CharField(max_length=50)
    description = models.TextField()
    date_created = models.DateTimeField(default= timezone.now)
    status = models.CharField(max_length=8, choices=ARTWORK_STATUS_CHOICES, default=FOR_SALE)
    likes = models.ManyToManyField(User, through='Like', related_name='Liker')

    def __str__(self):
        return self.title


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('artwork', 'user')


class Comment(models.Model):
    artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_commented = models.DateTimeField(default=timezone.now)
    comment = models.CharField(max_length=500, blank=False)
