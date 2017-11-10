from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.core.validators import MaxValueValidator, MinValueValidator


class Game(models.Model):
    '''Model of a video game'''
    title = models.CharField(max_length=255)
    developer = models.ForeignKey('Developer', null=True)
    publisher = models.ForeignKey('Publisher')
    genre = models.ForeignKey('Genre')
    platform = models.ForeignKey('Platform')
    OWN_STATUS_CHOICES = (
        ('Own', 'Own'),
        ('Want', 'Want'),
    )
    own_status = models.CharField(max_length=4, choices=OWN_STATUS_CHOICES, default='Want')
    PLAY_STATUS_CHOICES = (
        ('Played', 'Played'),
        ('Not Played', 'Not Played'),
    )
    play_status = models.CharField(max_length=10, choices=PLAY_STATUS_CHOICES, default='Not Played')
    personal_rating = models.IntegerField(
        validators = [MaxValueValidator(5), MinValueValidator(1)],
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('games:detail', kwargs={'pk': self.pk})


class Developer(models.Model):
    '''Model of a video game developer'''
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('developers:dev_detail', kwargs={'pk': self.pk})


class Publisher(models.Model):
    '''Model of a video game publisher'''
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('publishers:pub_detail', kwargs={'pk': self.pk})

class Genre(models.Model):
    '''Model of a video game genre'''
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Platform(models.Model):
    '''Model of a video game platform'''
    system = models.CharField(max_length=255)

    class Meta:
        ordering = ['system']

    def __str__(self):
        return self.system
