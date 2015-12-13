# -*- coding: utf-8 -*-
from django.db import models
from django.db.models.sql.aggregates import Count
from playchannel.managers import MovieManager

class Author(models.Model):
    first_name = models.CharField(verbose_name=u"Nome", max_length=50)
    last_name = models.CharField(verbose_name=u"Sobrenome", max_length=50)

    def __unicode__(self):
        return "{first_name} {last_name}".format(
            first_name= self.first_name,
            last_name=self.last_name
        )

    class Meta:
        verbose_name = u"Autor"
        verbose_name_plural = u"Autores"


class Genre(models.Model):

    title = models.CharField(verbose_name=u"Título", max_length=50)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u"Gênero"
        verbose_name_plural = u"Gêneros"


class Movie(models.Model):

    title = models.CharField(verbose_name=u"Título", max_length=100)
    synopsis = models.TextField(verbose_name=u"Sinópse")
    authors = models.ManyToManyField(Author, verbose_name=u"Autores")
    genres = models.ManyToManyField(Genre, verbose_name=u"Gênero")

    objects = MovieManager()

    def __unicode__(self):
        return self.title

    def get_related(self):
        target_geners = self.genres
        target_authors = self.authors
        related = self.objects.annotate(
            count_geners=Count('geners'),
            count_authors=Count('authors')
        ).filter(
            geners=target_geners,
            authos=target_authors
        ).order_by('count_geners', 'count_authors')
        return related

    class Meta:
        verbose_name = u"Filme"
        verbose_name_plural = u"Filmes"
