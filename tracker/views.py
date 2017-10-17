from django.core.urlresolvers import reverse_lazy
# from django.shortcuts import render
# from django.shortcuts import redirect
# from django.shortcuts import get_object_or_404
from django.views.generic import (
    ListView, DetailView,
    CreateView, UpdateView, DeleteView
)

from .models import Game
from .forms import GameForm

# # Create your views here.
# def tracker_table(request):
#     games = Game.objects.all()
#     return render(request, 'tracker/tracker_table.html', {'games':games})


class GameListView(ListView):
    context_object_name = 'games'
    model = Game


# def game_detail(request, pk):
#     game = get_object_or_404(Game, pk=pk)
#     return render(request, 'tracker/game_detail.html', {'game': game})
#

class GameDetailView(DetailView):
    model = Game


# def add_game(request):
#     if request.method == 'POST':
#         form = GameForm(request.POST)
#         if form.is_valid():
#             game = form.save(commit=False)
#             # TODO: Check if this game already exists in the database
#             game.save()
#             return redirect('tracker_table')
#     else:
#         form = GameForm()
#     return render(request, 'tracker/add_game.html', {'form':form})


class GameCreateView(CreateView):
    fields = ('publisher', 'title', 'platform', 'genre', 'own_status', 'play_status')
    model = Game
#
# def edit_game(request, pk):
#     game = get_object_or_404(Game, pk=pk)
#     if request.method == 'POST':
#         form = GameForm(request.POST, instance=game)
#         if form.is_valid():
#             game = form.save(commit=False)
#             # TODO: Check if this game already exists in the database
#             game.save()
#             # TODO: if editing from tracker table then go back to tracker table
#             # if editing from game detail page then go back to game detail page
#             return redirect('tracker_table')
#     else:
#         form = GameForm(instance=game)
#     return render(request, 'tracker/add_game.html', {'form':form})


class GameUpdateView(UpdateView):
    fields = ('publisher', 'title', 'platform', 'genre', 'own_status', 'play_status')
    model = Game

# def delete_game(request, pk):
#     game = get_object_or_404(Game, pk=pk)
#     game.delete()
#     return redirect('tracker_table')
#

class GameDeleteView(DeleteView):
    model = Game
    success_url = reverse_lazy("games:list")
