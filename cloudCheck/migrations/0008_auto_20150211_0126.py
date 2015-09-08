# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cloudCheck', '0007_image_iscloudy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='isCloudy',
            field=models.IntegerField(default=0, choices=[(0, b'Not checked yet'), (1, b'Cloud free'), (2, b'Needs user input'), (3, b'Unusable')]),
            preserve_default=True,
        ),
    ]
