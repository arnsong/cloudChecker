import os
from django.contrib.gis.utils import LayerMapping
from models import Image

from_shpfile = {
    'sensor' : 'SENSOR',
    'scene_id' : 'SCENE_ID',
    'status' : 'STATUS',
    'catalog_id' : 'CATALOG_ID',
    'order_id' : 'ORDER_ID',
    'acq_time' : 'ACQ_TIME',
    'prod_level' : 'PROD_LEVEL',
    'bands' : 'BANDS',
    'rows' : 'ROWS',
    'columns' : 'COLUMNS',
    'bits_pixel' : 'BITS_PIXEL',
    'output_fmt' : 'OUTPUT_FMT',
    'cloudcover' : 'CLOUDCOVER',
    'sun_elev' : 'SUN_ELEV',
    'scan_dir' : 'SCAN_DIR',
    'off_nadir' : 'OFF_NADIR',
    'meangsd' : 'MEANGSD',
    'ref_height' : 'REF_HEIGHT',
    'exposure' : 'EXPOSURE',
    'line_rate' : 'LINE_RATE',
    'spec_type' : 'SPEC_TYPE',
    'country' : 'COUNTRY',
    'cent_lat' : 'CENT_LAT',
    'cent_lon' : 'CENT_LONG',
    'o_filename' : 'O_FILENAME',
    'o_filepath' : 'O_FILEPATH',
    'o_drive' : 'O_DRIVE',
    'previewjpg' : 'PREVIEWJPG',
    'previewurl' : 'PREVIEWURL',
    'file_sz' : 'FILE_SZ',
    'mpoly' : 'MULTIPOLYGON',
}

img_shp = os.path.abspath('/rdebase/sea_ice/2015jan26/shapefile/deeb_chukchiseaice_2015jan23_imagery.shp')

def run(verbose=True):
    lm = LayerMapping(Image, img_shp, from_shpfile, transform=False, encoding='iso-8859-1')
    
    lm.save(strict=True, verbose=verbose)

