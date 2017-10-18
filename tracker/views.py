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
    highest_rated_game = Game.objects.order_by('-personal_rating').first()
    buy_next_game = Game.objects.filter(own_status='Want').last()

    def get_ordering(self):
        self.order = self.request.GET.get('order', default='asc')
        selected_ordering = self.request.GET.get('ordering', default='title')
        if self.order == "desc":
            selected_ordering = "-" + selected_ordering
        return selected_ordering

    def get_context_data(self, *args, **kwargs):
        context = super(GameListView, self).get_context_data(*args, **kwargs)
        context['current_order'] = self.get_ordering()
        context['order'] = self.order
        context['highest_rated_game'] = self.highest_rated_game
        context['buy_next_game'] = self.buy_next_game
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
