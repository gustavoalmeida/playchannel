# -*- coding: utf-8 -*-
import os
import uuid
from django.db import models
from django.db.models import Count, Q
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


def cover_upload(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('movie/cover', filename)

class Movie(models.Model):

    title = models.CharField(verbose_name=u"Título", max_length=100)
    synopsis = models.TextField(verbose_name=u"Sinópse")
    authors = models.ManyToManyField(Author, verbose_name=u"Autores")
    genres = models.ManyToManyField(Genre, verbose_name=u"Gênero")
    cover = models.ImageField(verbose_name=u"capa", upload_to=cover_upload)
    objects = MovieManager()

    def __unicode__(self):
        return self.title

    def get_relateds(self):
        target_genres = self.genres.all()
        target_authors = self.authors.all()
        related = Movie.objects.annotate(
            count_genres=Count('genres'),
            count_authors=Count('authors'),
        ).filter(
            Q(genres__id__in=[g.id for g in target_genres]) |
            Q(authors__id__in=[g.id for g in target_authors])
        ).order_by('-count_genres', '-count_authors')
        return related.exclude(id=self.pk)

    class Meta:
        verbose_name = u"Filme"
        verbose_name_plural = u"Filmes"
