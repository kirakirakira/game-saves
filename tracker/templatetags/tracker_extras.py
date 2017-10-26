from django import template
import random

from tracker.models import Game


register = template.Library()

@register.simple_tag
def highest_rated_game():
    '''Get the highest rated game that has been added to the tracker'''
    return Game.objects.order_by('-personal_rating').first()

@register.simple_tag
def buy_next_game():
    '''Returns a random game from tracker that is not owned'''
    want_games = Game.objects.filter(own_status='Want')
    random_index = random.randint(0, want_games.count() - 1)
    return want_games[random_index]

@register.simple_tag
def num_games_played():
    return Game.objects.filter(play_status='Played').count()

@register.simple_tag
def num_games_nplayed():
    return Game.objects.filter(play_status='Not Played').count()

@register.simple_tag
def num_games_own():
    return Game.objects.filter(own_status='Own').count()

@register.simple_tag
def num_games_want():
    return Game.objects.filter(own_status='Want').count()

@register.simple_tag
def tot_games_tracked():
    return Game.objects.all().count()
