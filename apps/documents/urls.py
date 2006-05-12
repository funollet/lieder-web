from django.conf.urls.defaults import *

obj_dict = {'app_label': 'documents', 'module_name': 'documents',}
categ_dict = {'app_label': 'documents', 'module_name': 'documentcategorys',}
categ_dict_slug = dict(categ_dict, slug_field='slug',)

urlpatterns = patterns('django.views.generic.list_detail',
    (r'^$', 'object_list', categ_dict, ),
    (r'^(?P<object_id>\d+)/$', 'object_detail', categ_dict, ),
    (r'^(?P<slug>[\w-]+)/$', 'object_detail', categ_dict_slug),
)

