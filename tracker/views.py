from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from .models import Game
from .forms import GameForm

# Create your views here.
def tracker_table(request):
    games = Game.objects.all()
    return render(request, 'tracker/tracker_table.html', {'games':games})


def add_game(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            game = form.save(commit=False)
            # TODO: Check if this game already exists in the database
            game.save()
            return redirect('tracker_table')
    else:
        form = GameForm()
    return render(request, 'tracker/add_game.html', {'form':form})


def edit_game(request, pk):
    game = get_object_or_404(Game, pk=pk)
    if request.method == 'POST':
        form = GameForm(request.POST, instance=game)
        if form.is_valid():
            game = form.save(commit=False)
            # TODO: Check if this game already exists in the database
            game.save()
            return redirect('tracker_table')
    else:
        form = GameForm(instance=game)
    return render(request, 'tracker/add_game.html', {'form':form})


def delete_game(request, pk):
    game = get_object_or_404(Game, pk=pk)
    game.delete()
    return redirect('tracker_table')
