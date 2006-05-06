from django.conf.urls.defaults import *

link_dict = {'app_label': 'links', 'module_name': 'links',}
categ_dict = {'app_label': 'links', 'module_name': 'linkcategorys',}


# object_id
urlpatterns = patterns('django.views.generic.list_detail',
    (r'^$', 'object_list', categ_dict),
    (r'^(?P<object_id>\d+)/$', 'object_detail', categ_dict,),
    (r'^(?P<slug>[\w-]+)/$', 'object_detail',
     dict(categ_dict, slug_field='slug')),
#    (r'^categories/$', 'object_list', categ_dict),
)
                       
