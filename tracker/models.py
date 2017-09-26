from django.db import models
from django.utils import timezone

# Create your models here.
class Game(models.Model):
    publisher = models.ForeignKey('Publisher')
    title = models.CharField(max_length=255)
    genre = models.ForeignKey('Genre')
    platform = models.ForeignKey('Platform')
    OWN_STATUS_CHOICES = (
        ('OWN', 'Own'),
        ('WANT', 'Want'),
    )
    PLAY_STATUS = (
        ('PLAYED', 'Played'),
        ('NOT PLAYED', 'Not Played'),
    )
    personal_rating = models.IntegerField()

    def __str__(self):
        return self.title


class Publisher(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Platform(models.Model):
    system = models.CharField(max_length=255)

    def __str__(self):
        return self.system
