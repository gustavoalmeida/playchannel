# -*- coding: utf-8 -*-
import os
import uuid
from autoslug import AutoSlugField
from django.db import models
from django.db.models import Count, Q
from playchannel.managers import MovieManager

class Actor(models.Model):
    first_name = models.CharField(verbose_name=u"Nome", max_length=50)
    last_name = models.CharField(verbose_name=u"Sobrenome", max_length=50)
    slug = AutoSlugField(populate_from='get_full_name', blank=True, null=True)

    def get_full_name(self):
        return u"{} {}".format(self.first_name, self.last_name)

    def __unicode__(self):
        return "{first_name} {last_name}".format(
            first_name= self.first_name,
            last_name=self.last_name
        )

    class Meta:
        verbose_name = u"Ator"
        verbose_name_plural = u"Atores"


class Genre(models.Model):

    title = models.CharField(verbose_name=u"Título", max_length=50)
    slug = AutoSlugField(populate_from='title', blank=True, null=True)

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
    slug = AutoSlugField(populate_from='title', blank=True, null=True)
    synopsis = models.TextField(verbose_name=u"Sinópse")
    actors = models.ManyToManyField(Actor, verbose_name=u"Atores")
    genres = models.ManyToManyField(Genre, verbose_name=u"Gênero")
    cover = models.ImageField(verbose_name=u"capa", upload_to=cover_upload)
    objects = MovieManager()

    def __unicode__(self):
        return self.title

    def get_relateds(self):
        target_genres = self.genres.all()
        target_actors = self.actors.all()
        related = Movie.objects.annotate(
            count_genres=Count('genres'),
            count_actors=Count('actors'),
        ).filter(
            Q(genres__id__in=[g.id for g in target_genres]) |
            Q(actors__id__in=[g.id for g in target_actors])
        ).order_by('-count_genres', '-count_actors')
        return related.exclude(id=self.pk)

    class Meta:
        verbose_name = u"Filme"
        verbose_name_plural = u"Filmes"

    def delete(self, *args, **kwargs):
        if kwargs.pop('include_images', False):
            for field in self._meta.fields:
                if type(field) == models.ImageField:
                    image = self.__getattribute__(field.name)
                    if image.name != '':
                        image.storage.delete(image.name)
        super(Movie, self).delete(*args, **kwargs)
