from django.conf.urls import patterns, include, url
from playchannel.views import ( MovieListView, GenreListView, ActorListView,
                                MovieDetailView, GenreDetailView, ActorDetailView )
urlpatterns = patterns('',
    url(r'^$', MovieListView.as_view(), name='home'),
    url(r'^filme/$', MovieListView.as_view(), name='movie-list'),
    url(r'^filme/(?P<slug>[0-9a-z\-]+)/$', MovieDetailView.as_view(), name='movie-detail'),
    url(r'^genero/$', GenreListView.as_view(), name='genre-list'),
    url(r'^genero/(?P<slug>[0-9a-z\-]+)/$', GenreDetailView.as_view(), name='genre-detail'),
    url(r'^autor/$', ActorListView.as_view(), name='actor-list'),
    url(r'^autor/(?P<slug>[0-9a-z\-]+)/$', ActorDetailView.as_view(), name='actor-detail'),
)
