from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.tracker_table, name='tracker_table'),
    url(r'^new/$', views.add_game, name='add_game'),
    url(r'^edit/(?P<pk>\d+)/$', views.edit_game, name='edit_game'),
    url(r'^delete/(?P<pk>\d+)/$', views.delete_game, name='delete_game'),
]
