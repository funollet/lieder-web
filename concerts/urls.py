from django.conf.urls.defaults import *
from datetime import datetime
from concerts.models import Concert

# Return only objects with a future 'pub_date'.
info_dict = {
    'queryset': Concert.objects.all() ,
    'allow_empty': True,
}

info_dict_slug = dict(info_dict, slug_field='slug')

urlpatterns = patterns('',
    (r'^$', 'concerts.views.futureitems_object_list', info_dict),
    (r'^(?P<slug>[\w-]+)/$', 'django.views.generic.list_detail.object_detail', info_dict_slug),
)


