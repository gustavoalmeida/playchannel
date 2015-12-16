# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playchannel', '0004_auto_20151216_0011'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Author',
        ),
    ]
