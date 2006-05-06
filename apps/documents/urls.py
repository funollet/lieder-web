from django.conf.urls.defaults import *

obj_dict = {'app_label': 'documents', 'module_name': 'documents',}
categ_dict = {'app_label': 'documents', 'module_name': 'documentcategorys',}


# object_id
urlpatterns = patterns('django.views.generic.list_detail',
    (r'^$', 'object_list', obj_dict, ),
    (r'^categ/$', 'object_list', categ_dict, ),
    (r'^categ/(?P<object_id>\d+)/$', 'object_detail', categ_dict, ),
    (r'^categ/(?P<slug>[\w-]+)/$', 'object_detail', 
    dict(categ_dict, slug_field='slug',),
    ),
)
                       
