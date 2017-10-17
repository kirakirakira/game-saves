from django.core.urlresolvers import reverse_lazy
from django.views.generic import (
    ListView, DetailView,
    CreateView, UpdateView, DeleteView
)

from .models import Game
from .forms import GameForm


class GameListView(ListView):
    context_object_name = 'games'
    model = Game


class GameDetailView(DetailView):
    model = Game


class GameCreateView(CreateView):
    fields = ('publisher', 'title', 'platform', 'genre', 'own_status', 'play_status', 'personal_rating')
    model = Game


class GameUpdateView(UpdateView):
    fields = ('publisher', 'title', 'platform', 'genre', 'own_status', 'play_status', 'personal_rating')
    model = Game


class GameDeleteView(DeleteView):
    model = Game
    success_url = reverse_lazy("games:list")
