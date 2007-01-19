from django.conf.urls.defaults import *
from links.models import Link, LinkCategory

link_dict = {'queryset': Link.objects.all() }
link_dict_slug = dict(link_dict, slug_field='slug')
categ_dict = {'queryset': LinkCategory.objects.all() }
categ_dict_slug = dict(categ_dict, slug_field='slug')

urlpatterns = patterns('django.views.generic.list_detail',
    (r'^$', 'object_list', categ_dict),
    (r'^(?P<slug>[\w-]+)/$', 'object_detail', categ_dict_slug),
    (r'^[\w-]+/(?P<slug>[\w-]+)/$', 'object_detail', link_dict_slug),
)

