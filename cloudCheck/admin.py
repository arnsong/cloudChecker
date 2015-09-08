from django.contrib import admin
from cloudCheck.models import Image

# Register your models here.
admin.site.register(Image)
admin.AdminSite.site_header = 'Sea ice imagery administration'
admin.AdminSite.site_title  = 'Sea ice images admin'
