from django.conf.urls.defaults import *
from lieder.apps.programmes.models import Programme

info_dict = { 'queryset': Programme.objects.all() }

# object_id
urlpatterns = patterns('django.views.generic.list_detail',
    (r'^$', 'object_list', info_dict),
    (r'^(?P<object_id>\d+)/$', 'object_detail', info_dict,),
    (r'^(?P<slug>[\w-]+)/$', 'object_detail', dict(info_dict, slug_field='slug') ),
)
                       
