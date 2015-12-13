import os
from model_mommy import mommy
from django.core.urlresolvers import reverse
from django.core.files.base import File

from django.test import TestCase
from playchannel.models import Movie, Genre, Author

class TestMovie(TestCase):

    def setUp(self):
        self.genres = mommy.make(Genre, _quantity=3)
        self.authors = mommy.make(Author, _quantity=3)
        self.movies = mommy.make(Movie, genres=self.genres,
                                authors=self.authors,
                                _quantity=20)

    def test_cover_field(self):
        movie = mommy.make(Movie)
        movie.cover = File(open(os.path.join(os.path.dirname(__file__),"data","cover.png")))
        movie.save()
        p = Movie.objects.get(id=movie.id).cover.path
        self.failUnless(open(p), 'file not found')


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

    def test_related_movies(self):
        sample_movie = self.movies[0]
        related = sample_movie.get_relateds()
        self.assertEqual(related.count(), 19)
        for m in self.movies:
            m.delete()
        first_movie = mommy.make(Movie,
                                 authors=[self.authors[0]],
                                 genres=[self.genres[0]]
                                 )
        second_movie = mommy.make(Movie,
                                  genres=[self.genres[0]])
        third_movie = mommy.make(Movie,
                                 authors=[self.authors[0]],
                                 genres=[self.genres[0]])
        related = first_movie.get_relateds()
        self.assertEqual(related[0].title, third_movie.title)
        self.assertEqual(len(related), 2)
        self.assertEqual(related[1].title, second_movie.title)

    def test_view_home(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)