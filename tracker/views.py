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
    num_games_played = Game.objects.filter(play_status='Played').count()
    num_games_nplayed = Game.objects.filter(play_status='Not Played').count()
    num_games_own = Game.objects.filter(own_status='Own').count()
    num_games_want = Game.objects.filter(own_status='Want').count()
    tot_games_tracked = Game.objects.all().count()

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
        context['num_games_played'] = self.num_games_played
        context['num_games_nplayed'] = self.num_games_nplayed
        context['num_games_own'] = self.num_games_own
        context['num_games_want'] = self.num_games_want
        context['tot_games_tracked'] = self.tot_games_tracked
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
