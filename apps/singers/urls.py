from django.conf.urls.defaults import *

info_dict = {
    'app_label': 'singers',
    'module_name': 'singers',
}

urlpatterns = patterns('django.views.generic.list_detail',
    (r'^$', 'object_list', info_dict),
)
                       
