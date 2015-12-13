from django.shortcuts import render
from django.views.generic import ListView
from playchannel.models import Movie


class MovieListView(ListView):
    model = Movie
