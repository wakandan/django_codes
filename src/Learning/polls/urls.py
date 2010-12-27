from django.conf.urls.defaults import *
from polls.models import Poll

info_dict = {
    'queryset': Poll.objects.all(),
}

urlpatterns = patterns('',
    url(r'^$', 'django.views.generic.list_detail.object_list', 
         dict(info_dict, template_name='index.html'),
         'index'),
    url(r'^(?P<object_id>\d+)/$', 
        'django.views.generic.list_detail.object_detail', 
        dict(info_dict, template_name='detail.html'),
        'detail'),
    url(r'^(?P<object_id>\d+)/results/$', 
        'django.views.generic.list_detail.object_detail', 
        dict(info_dict, template_name='results.html'), 
        'poll_results'),
    (r'^(?P<poll_id>\d+)/vote/$', 'polls.views.vote'),
)
