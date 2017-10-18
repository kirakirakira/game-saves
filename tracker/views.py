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

    def get_ordering(self):
        self.order = self.request.GET.get('order', 'asc')
        selected_ordering = self.request.GET.get('ordering', 'title')
        if self.order == "desc":
            selected_ordering = "-" + selected_ordering
        return selected_ordering

    def get_context_data(self, *args, **kwargs):
        context = super(GameListView, self).get_context_data(*args, **kwargs)
        context['current_order'] = self.get_ordering()
        context['order'] = self.order
        return context


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
