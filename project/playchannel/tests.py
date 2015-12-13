from model_mommy import mommy
from django.test import TestCase
from playchannel.models import Movie, Genre, Author

class TestMovie(TestCase):

    def test_movie_model(self):
        genres = mommy.make(Genre, _quantity=3)
        authors = mommy.make(Author, _quantity=3)
        movie = mommy.make(Movie, genres=genres, authors=authors)