# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cloudCheck', '0002_auto_20150211_0109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cloud',
            name='date_checked',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 11, 1, 10, 51, 258312, tzinfo=utc), verbose_name=b'Date checked'),
            preserve_default=True,
        ),
    ]
