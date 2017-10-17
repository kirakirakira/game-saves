from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.GameListView.as_view(), name='list'),
    url(r'^game/(?P<pk>\d+)$', views.GameDetailView.as_view(), name='detail'),
    url(r'^create/$', views.GameCreateView.as_view(), name='create'),
    url(r'^edit/(?P<pk>\d+)/$', views.GameUpdateView.as_view(), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', views.GameDeleteView.as_view(), name='delete'),
]
