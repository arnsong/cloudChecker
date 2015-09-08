from django.conf.urls import patterns, include, url
from cloudCheck import views
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from geodjango import settings

urlpatterns = patterns('', 
    url(r'^$', views.index, name='index' ),
    url(r'^cloud_submit/(?P<image_id>\d+)', views.cloud_submit),
                       
) 
