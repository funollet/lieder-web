from django.conf.urls.defaults import *
from datetime import datetime
from lieder.apps.concerts.models import Concert

# Return only objects with a future 'pub_date'.
info_dict = { 'queryset': Concert.objects.filter(pub_date__gt=str(datetime.now())) }

info_dict_slug = dict(info_dict, slug_field='slug')

urlpatterns = patterns('django.views.generic.list_detail',
    (r'^$', 'object_list', info_dict),
    (r'^(?P<slug>[\w-]+)/$', 'object_detail', info_dict_slug),
)
                       
