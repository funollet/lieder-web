from django.conf.urls.defaults import *
from datetime import datetime

info_dict = {'app_label': 'concerts', 'module_name': 'concerts',
    # Return only objects with a future 'pub_date'.
    'extra_lookup_kwargs': {'pub_date__gt': str(datetime.now())},
}
info_dict_slug = dict(info_dict, slug_field='slug')

urlpatterns = patterns('django.views.generic.list_detail',
    (r'^$', 'object_list', info_dict),
    (r'^(?P<slug>[\w-]+)/$', 'object_detail', info_dict_slug),
)
                       
