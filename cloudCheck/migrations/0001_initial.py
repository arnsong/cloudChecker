# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import django.contrib.gis.db.models.fields
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cloud',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cloud_class', models.IntegerField(default=0, verbose_name=b'Cloud classification')),
                ('comment', models.CharField(default=b' ', max_length=140, verbose_name=b'Comment')),
                ('checked_by', models.CharField(default=b' ', max_length=32, verbose_name=b'Checked by')),
                ('date_checked', models.DateTimeField(default=datetime.datetime(2015, 2, 11, 1, 9, 1, 844125, tzinfo=utc), verbose_name=b'Date checked')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sensor', models.CharField(max_length=12, verbose_name=b'Sensor')),
                ('scene_id', models.CharField(max_length=48, verbose_name=b'Scene ID')),
                ('status', models.CharField(max_length=16, verbose_name=b'Status')),
                ('catalog_id', models.CharField(max_length=32, verbose_name=b'Catalog ID')),
                ('order_id', models.CharField(max_length=32, verbose_name=b'Order ID')),
                ('acq_time', models.CharField(max_length=32, verbose_name=b'Acquisition time')),
                ('prod_level', models.CharField(max_length=6, verbose_name=b'Prod level')),
                ('bands', models.IntegerField(verbose_name=b'Number of bands')),
                ('rows', models.IntegerField(verbose_name=b'Number of rows')),
                ('columns', models.IntegerField(verbose_name=b'Number of columns')),
                ('bits_pixel', models.IntegerField(verbose_name=b'Bit depth')),
                ('output_fmt', models.CharField(max_length=8, verbose_name=b'Output format')),
                ('cloudcover', models.FloatField(verbose_name=b'% cloud cover')),
                ('sun_elev', models.FloatField(verbose_name=b'Sun elevation')),
                ('scan_dir', models.CharField(max_length=12, verbose_name=b'Scan direction')),
                ('off_nadir', models.FloatField()),
                ('meangsd', models.FloatField()),
                ('ref_height', models.FloatField()),
                ('exposure', models.FloatField()),
                ('line_rate', models.FloatField()),
                ('spec_type', models.CharField(max_length=16, verbose_name=b'Spec type')),
                ('country', models.CharField(max_length=4, verbose_name=b'Country code')),
                ('cent_lat', models.FloatField(verbose_name=b'Center latitude')),
                ('cent_lon', models.FloatField(verbose_name=b'Center longitude')),
                ('o_filename', models.CharField(max_length=96, verbose_name=b'Original filename')),
                ('o_filepath', models.CharField(max_length=254, verbose_name=b'Original path')),
                ('o_drive', models.CharField(max_length=16, verbose_name=b'Original drive')),
                ('previewjpg', models.CharField(max_length=254, verbose_name=b'Preview jpg filename')),
                ('previewurl', models.CharField(max_length=254, verbose_name=b'Preview jpg url')),
                ('file_sz', models.FloatField(verbose_name=b'File size')),
                ('isCloudy', models.IntegerField(default=2, choices=[(0, b'Cloud free'), (1, b'Needs user input'), (2, b'Unusable')])),
                ('mpoly', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
