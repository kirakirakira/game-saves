from django.contrib import admin
from .models import Game, Publisher, Genre, Platform, Developer


class GameAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        '''Alphabetically order the platform, genre, publisher, and developer choices.'''
        if db_field.name=='platform':
            kwargs["queryset"]=Platform.objects.order_by('system')
        if db_field.name=='genre':
            kwargs["queryset"]=Genre.objects.order_by('name')
        if db_field.name=='publisher':
            kwargs["queryset"]=Publisher.objects.order_by('name')
        if db_field.name == 'developer':
            kwargs["queryset"]=Developer.objects.order_by('name')
        return super(GameAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


# Register models
admin.site.register(Game, GameAdmin)
admin.site.register(Publisher)
admin.site.register(Genre)
admin.site.register(Platform)
admin.site.register(Developer)
