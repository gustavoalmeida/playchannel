from django.shortcuts import render
from django.views.generic import ListView, DetailView
from playchannel.models import Movie, Genre, Actor


class MovieListView(ListView):
    model = Movie


class GenreListView(ListView):
    model = Genre


class ActorListView(ListView):
    model = Actor


class MovieDetailView(DetailView):
    model = Movie


class GenreDetailView(DetailView):
    model = Genre


class ActorDetailView(DetailView):
    model = Actor