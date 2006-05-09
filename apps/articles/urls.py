from django.conf.urls.defaults import *

obj_dict = {'app_label': 'articles', 'module_name': 'articles', }
section_dict = {'app_label': 'articles', 'module_name': 'sections', }


urlpatterns = patterns('lieder.apps.misc.views',
    (r'^$', 'limited_object_list', section_dict, ),
    (r'^section/$', 'limited_object_list', section_dict,),
    (r'^section/(?P<object_id>\d+)/$', 'limited_object_detail', section_dict,),
    (r'^(?P<object_id>\d+)/$', 'limited_object_detail', obj_dict,),
    (r'^(?P<slug>[\w-]+)/$', 'limited_object_detail', dict(obj_dict, slug_field='slug')),
)
