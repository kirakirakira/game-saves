from django.contrib import admin
from .models import Game, Publisher, Genre, Platform

# Register your models here.
admin.site.register(Game)
admin.site.register(Publisher)
admin.site.register(Genre)
admin.site.register(Platform)
