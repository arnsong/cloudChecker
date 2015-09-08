# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cloudCheck', '0011_auto_20150212_0032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='checked_by',
        ),
        migrations.RemoveField(
            model_name='image',
            name='checked_date',
        ),
        migrations.RemoveField(
            model_name='image',
            name='cloud_comment',
        ),
        migrations.RemoveField(
            model_name='image',
            name='is_cloudy',
        ),
    ]
