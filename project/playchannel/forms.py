#-*- coding: utf-8 -*-
from django import forms
from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions

from playchannel.models import Movie


class MovieAdminForm(forms.ModelForm):

    def clean_cover(self):
        cleaned_data = self.cleaned_data
        cover = cleaned_data.get('cover', None)
        if cover:
            fname, dot, extension = cover.name.rpartition('.')
            if extension.lower() not in ['jpg', 'jpeg', 'gif', 'png']:
                raise ValidationError(u"O formato da imagem da capar enviada não parece válido.")
            w,h = get_image_dimensions(cover)
            if w != 130 or h != 90:
                raise ValidationError(u"O tamanho da imagem do campo capa enviada não parece válido.")
        return cover

    class Meta:
        model = Movie
        exclude = []