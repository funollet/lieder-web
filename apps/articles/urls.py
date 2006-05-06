from django.conf.urls.defaults import *

info_dict = {
    'app_label': 'articles',
    'module_name': 'articles',
}


urlpatterns = patterns('lieder.apps.misc.views',
    (r'^$', 'limited_object_list', info_dict, ),
    (r'^(?P<object_id>\d+)/$', 'limited_object_detail', info_dict,),
    (r'^(?P<slug>[\w-]+)/$', 'limited_object_detail', dict(info_dict, slug_field='slug')),
)
                       
