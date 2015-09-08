# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cloudCheck', '0006_remove_image_iscloudy'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='isCloudy',
            field=models.IntegerField(default=2, choices=[(0, b'Cloud free'), (1, b'Needs user input'), (2, b'Unusable')]),
            preserve_default=True,
        ),
    ]
