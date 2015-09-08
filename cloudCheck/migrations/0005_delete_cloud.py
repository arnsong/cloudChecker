# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cloudCheck', '0004_auto_20150211_0112'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cloud',
        ),
    ]
