# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import playchannel.models


class Migration(migrations.Migration):

    dependencies = [
        ('playchannel', '0002_auto_20151213_0248'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='cover',
            field=models.ImageField(default='movie/no-cover.png', upload_to=playchannel.models.cover_upload, verbose_name='capa'),
            preserve_default=False,
        ),
    ]
