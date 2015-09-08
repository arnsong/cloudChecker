from django.contrib.gis.db import models
from django.forms import ModelForm
import datetime

# Create your models here.
NCHK = 0
GOOD = 1
PART = 2
NOGD = 3

CLOUDCOVER_CLASSIFICATION = ( ( NCHK, 'Not checked yet' ),
                              ( GOOD, 'Cloud free' ),
                              ( PART, 'Needs user input' ),
                              ( NOGD, 'Unusable' ),
                            )


class Image(models.Model):

    sensor     = models.CharField('Sensor', max_length=12)
    scene_id   = models.CharField('Scene ID', max_length=48)
    status     = models.CharField('Status', max_length=16)
    catalog_id = models.CharField('Catalog ID', max_length=32)
    order_id   = models.CharField('Order ID', max_length=32)
    acq_time   = models.CharField('Acquisition time', max_length=32)
    prod_level = models.CharField('Prod level', max_length=6)
    bands      = models.IntegerField('Number of bands')
    rows       = models.IntegerField('Number of rows')
    columns    = models.IntegerField('Number of columns')
    bits_pixel = models.IntegerField('Bit depth')
    output_fmt = models.CharField('Output format', max_length=8)
    cloudcover = models.FloatField('% cloud cover')
    sun_elev   = models.FloatField('Sun elevation')
    scan_dir   = models.CharField('Scan direction', max_length=12)
    off_nadir  = models.FloatField()
    meangsd    = models.FloatField()
    ref_height = models.FloatField()
    exposure   = models.FloatField()
    line_rate  = models.FloatField()
    spec_type  = models.CharField('Spec type', max_length=16)
    country    = models.CharField('Country code', max_length=4)
    cent_lat   = models.FloatField('Center latitude')
    cent_lon   = models.FloatField('Center longitude')
    o_filename = models.CharField('Original filename', max_length=96)
    o_filepath = models.CharField('Original path', max_length=254)
    o_drive    = models.CharField('Original drive', max_length=16)
    previewjpg = models.CharField('Preview jpg filename', max_length=254)
    previewurl = models.CharField('Preview jpg url', max_length=254)
    file_sz    = models.FloatField('File size')

    is_cloudy = models.IntegerField(choices=CLOUDCOVER_CLASSIFICATION, default=NCHK)
    cloud_comment = models.CharField(max_length=140, blank=True)
    checked_by   = models.CharField(max_length=32, blank=True)
    checked_date = models.DateTimeField(default=datetime.datetime.now(), blank=True)

    lock = models.BooleanField(default=False)

    mpoly = models.MultiPolygonField()
    objects = models.GeoManager()

    def __unicode__(self):
        return self.scene_id
