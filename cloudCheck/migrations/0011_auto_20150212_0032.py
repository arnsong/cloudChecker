# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cloudCheck', '0010_image_cloudsdatechecked'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='cloudsCheckedBy',
            new_name='checked_by',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='isCloudy',
            new_name='is_cloudy',
        ),
        migrations.RemoveField(
            model_name='image',
            name='cloudsDateChecked',
        ),
        migrations.AddField(
            model_name='image',
            name='checked_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 12, 0, 32, 27, 68092), blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='image',
            name='cloud_comment',
            field=models.CharField(max_length=140, blank=True),
            preserve_default=True,
        ),
    ]
