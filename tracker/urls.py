from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.GameListView.as_view(), name='list'),
    url(r'^game/(?P<pk>\d+)$', views.GameDetailView.as_view(), name='detail'),
    url(r'^create/$', views.GameCreateView.as_view(), name='create'),
    url(r'^edit/(?P<pk>\d+)/$', views.GameUpdateView.as_view(), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', views.GameDeleteView.as_view(), name='delete'),
    url(r'^developer/create/$', views.DeveloperCreateView.as_view(), name='dev_create'),
    url(r'^developer/detail/(?P<pk>\d+)$', views.DeveloperDetailView.as_view(), name='dev_detail'),
    url(r'^developer/list/$', views.DeveloperListView.as_view(), name='dev_list'),
    url(r'^developer/edit/(?P<pk>\d+)$', views.DeveloperUpdateView.as_view(), name='dev_update'),
    url(r'^developer/delete/(?P<pk>\d+)$', views.DeveloperDeleteView.as_view(), name='dev_delete'),
]
