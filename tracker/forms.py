from django import forms

from .models import Game


class GameForm(forms.ModelForm):

    class Meta:
        model = Game
        fields = ('publisher', 'title', 'genre', 'platform', 'own_status', 'play_status', 'personal_rating',)


# TODO: Create a formset so that you can add more than 1 game at a time
GameFormSet = forms.modelformset_factory(
    Game,
    form=GameForm,
    extra=5
)
