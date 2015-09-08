# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cloudCheck', '0008_auto_20150211_0126'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='cloudsCheckedBy',
            field=models.CharField(max_length=32, blank=True),
            preserve_default=True,
        ),
    ]
