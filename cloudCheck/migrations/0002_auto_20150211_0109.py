# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cloudCheck', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cloud',
            name='date_checked',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 11, 1, 9, 20, 358842, tzinfo=utc), verbose_name=b'Date checked'),
            preserve_default=True,
        ),
    ]
