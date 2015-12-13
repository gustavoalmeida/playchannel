from model_mommy import mommy
from django.test import TestCase
from playchannel.models import Movie, Genre, Author

class TestMovie(TestCase):

    def setUp(self):
        self.genres = mommy.make(Genre, _quantity=3)
        self.authors = mommy.make(Author, _quantity=3)
        self.movie = mommy.make(Movie, genres=self.genres,
                                authors=self.authors, _quantity=20)

    def test_movie_order_asc(self):
        movies_asc = Movie.objects.all().order_by('title')
        movies_asc_manager = Movie.objects.ordered_asc()
        for i in [1,5,10,15,20]:
            self.assertEqual(movies_asc[i-1].title, movies_asc_manager[i-1].title)
            self.assertEqual(movies_asc[i-1].title, movies_asc_manager[i-1].title)

    def test_movie_order_desc(self):
        movies_desc = Movie.objects.all().order_by('-title')
        movies_desc_manager = Movie.objects.ordered_desc()
        for i in [1,5,10,15,20]:
            self.assertEqual(movies_desc[i-1].title, movies_desc_manager[i-1].title)
            self.assertEqual(movies_desc[i-1].title, movies_desc_manager[i-1].title)

    def related_movies(self):
        sample_movie = self.movie.first()
        related = sample_movie.get_relateds()
        self.assertEqual(related.count(), 19)