from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^Learning/', include('Learning.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     (r'^admin/', include(admin.site.urls)),
     (r'^polls/', include('polls.urls')),
#     (r'^cms/', include('cms.urls')),
    (r'^cms/',include('cms.urls')),
    (r'^static/(?P<path>.*)$','django.views.static.serve',
        {'document_root':'/media/Data/My_Documents/Programming/Django/src/Learning/static'}),
    (r'^search/$','search.views.search'),
    (r'^coltrane/',include('coltrane.urls'))

)
