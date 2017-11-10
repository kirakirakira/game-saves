from django.core.urlresolvers import reverse_lazy
from django.views.generic import (
    ListView, DetailView,
    CreateView, UpdateView, DeleteView
)

from .models import Game
from .models import Developer
from .models import Publisher


class GameListView(ListView):
    '''List view of all video games in the tracker'''
    context_object_name = 'games'
    model = Game

    def get_ordering(self):
        '''Able to switch the ordering from ascending to descending and vice versa'''
        self.order = self.request.GET.get('order', default='asc')
        selected_ordering = self.request.GET.get('ordering', default='title')
        if self.order == "desc":
            selected_ordering = "-" + selected_ordering
        return selected_ordering

    def get_context_data(self, *args, **kwargs):
        context = super(GameListView, self).get_context_data(*args, **kwargs)
        context['current_order'] = self.get_ordering()
        context['order'] = self.order
        return context

    def get_queryset(self):
        '''Function to get queryset for the search bar'''
        qs = super().get_queryset()
        try:
            q = Game.objects.filter(title__icontains=self.request.GET['q'])
            return q
        except:
            return qs


class GameDetailView(DetailView):
    model = Game


class GameCreateView(CreateView):
    fields = ('title', 'developer', 'publisher', 'platform', 'genre', 'own_status', 'play_status', 'personal_rating')
    model = Game


class GameUpdateView(UpdateView):
    fields = ('title', 'developer', 'publisher', 'platform', 'genre', 'own_status', 'play_status', 'personal_rating')
    model = Game


class GameDeleteView(DeleteView):
    model = Game
    success_url = reverse_lazy("games:list")


class DeveloperCreateView(CreateView):
    fields = ('name',)
    model = Developer


class DeveloperDetailView(DetailView):
    model = Developer


class DeveloperListView(ListView):
    context_object_name = 'developers'
    model = Developer


class PublisherCreateView(CreateView):
    fields = ('name',)
    model = Publisher


class PublisherDetailView(DetailView):
    model = Publisher


class PublisherListView(ListView):
    context_object_name = 'publishers'
    model = Publisher
