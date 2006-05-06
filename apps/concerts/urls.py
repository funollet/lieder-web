from django.conf.urls.defaults import *

info_dict = {
    'app_label': 'concerts',
    'module_name': 'concerts',
}

# object_id
urlpatterns = patterns('django.views.generic.list_detail',
    (r'^$', 'object_list', info_dict),
    (r'^(?P<object_id>\d+)/$', 'object_detail', info_dict,),
    (r'^(?P<slug>[\w-]+)/$', 'object_detail', dict(info_dict, slug_field='slug')),
)
                       
