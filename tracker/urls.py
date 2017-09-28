from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.tracker_table, name='tracker_table')
]
