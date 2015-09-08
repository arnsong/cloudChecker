# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cloudCheck', '0009_image_cloudscheckedby'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='cloudsDateChecked',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 11, 2, 0, 12, 69627), blank=True),
            preserve_default=True,
        ),
    ]
