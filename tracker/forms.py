from django import forms

from .models import Game


class GameForm(forms.ModelForm):

    class Meta:
        model = Game
        fields = ('publisher', 'title', 'genre', 'platform', 'own_status', 'play_status', 'personal_rating',)
