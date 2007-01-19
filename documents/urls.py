from django.conf.urls.defaults import *
from documents.models import Document, DocumentCategory

obj_dict = { 'queryset': Document.objects.all() }
obj_dict_slug =  dict(obj_dict, slug_field='slug',)
categ_dict = { 'queryset': DocumentCategory.objects.all() }
categ_dict_slug = dict(categ_dict, slug_field='slug',)

urlpatterns = patterns('django.views.generic.list_detail',
    (r'^$', 'object_list', categ_dict, ),
    (r'^(?P<object_id>\d+)/$', 'object_detail', categ_dict, ),
    (r'^(?P<slug>[\w-]+)/$', 'object_detail', categ_dict_slug),
    (r'^[\w-]+/(?P<slug>[\w-]+)/$', 'object_detail', obj_dict_slug),
)

