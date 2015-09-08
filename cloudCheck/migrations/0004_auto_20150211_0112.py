# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cloudCheck', '0003_auto_20150211_0110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cloud',
            name='date_checked',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 11, 1, 12, 36, 977035, tzinfo=utc), verbose_name=b'Date checked'),
            preserve_default=True,
        ),
    ]
