# -*- coding: utf-8 -*-
from django.db import models

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
    genre = models.ManyToManyField(Genre, verbose_name=u"Gênero")

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u"Filme"
        verbose_name_plural = u"Filmes"
