from django.shortcuts import render
from .models import Game

# Create your views here.
def tracker_table(request):
    games = Game.objects.all()
    return render(request, 'tracker/tracker_table.html', {'games':games})
