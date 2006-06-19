from django.conf.urls.defaults import *

link_dict = {'queryset': Link.objects.all() }
categ_dict = {'queryset': LinkCategory.objects.all() }
categ_dict_slug = dict(categ_dict, slug_field='slug')

urlpatterns = patterns('django.views.generic.list_detail',
    (r'^$', 'object_list', categ_dict),
    (r'^(?P<object_id>\d+)/$', 'object_detail', categ_dict,),
    (r'^(?P<slug>[\w-]+)/$', 'object_detail', categ_dict_slug),
)
