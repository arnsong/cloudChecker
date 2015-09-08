# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cloudCheck', '0012_auto_20150212_0047'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='checked_by',
            field=models.CharField(max_length=32, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='image',
            name='checked_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 12, 0, 53, 0, 628381), blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='image',
            name='cloud_comment',
            field=models.CharField(max_length=140, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='image',
            name='is_cloudy',
            field=models.IntegerField(default=0, choices=[(0, b'Not checked yet'), (1, b'Cloud free'), (2, b'Needs user input'), (3, b'Unusable')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='image',
            name='lock',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
