from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.tracker_table, name='tracker_table'),
    url(r'^new/$', views.add_game, name='add_game'),
    url(r'^new/(?P<pk>\d+)/$', views.edit_game, name='edit_game'),
]
