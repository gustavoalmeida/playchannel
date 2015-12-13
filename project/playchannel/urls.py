from django.conf.urls import patterns, include, url
from playchannel.views import MovieListView
urlpatterns = patterns('',
    url(r'^$', MovieListView.as_view(), name='home'),
)
