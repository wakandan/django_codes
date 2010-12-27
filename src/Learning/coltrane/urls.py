'''
Created on Dec 26, 2010

@author: akai
'''
from django.conf.urls.defaults import *
from django.contrib import admin
from models import Entry

admin.autodiscover()
info_dict = {
    'queryset':Entry.objects.all()    
}

urlpatterns = patterns('',
    url(r'^$','django.views.generic.list_detail.object_list',
        dict(info_dict, template_name='coltrane_index.html'),
        'coltrane_index'),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[\w-]+)/$',
        'django.views.generic.date_based.object_detail',
        dict(info_dict, template_name='coltrane_detail.html',
             date_field='pub_date'),
        'coltrane_detail'),
    url(r'^(?P<year>\d{4})/$',
        'django.views.generic.date_based.archive_year',
        dict(info_dict, template_name='coltrane_archive_year.html',
             make_object_list=True, date_field='pub_date'))
)
