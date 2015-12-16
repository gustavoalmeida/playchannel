# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('playchannel', '0005_delete_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='slug',
            field=autoslug.fields.AutoSlugField(populate_from=b'get_full_name', null=True, editable=False, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='genre',
            name='slug',
            field=autoslug.fields.AutoSlugField(populate_from=b'title', null=True, editable=False, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='movie',
            name='slug',
            field=autoslug.fields.AutoSlugField(populate_from=b'title', null=True, editable=False, blank=True),
            preserve_default=True,
        ),
    ]
