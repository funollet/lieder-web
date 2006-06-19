from django.conf.urls.defaults import *
from lieder.apps.documents.models import Document, DocumentCategory

obj_dict = { 'queryset': Document.objects.all() }
categ_dict = { 'queryset': DocumentCatergory.objects.all() }
categ_dict_slug = dict(categ_dict, slug_field='slug',)

urlpatterns = patterns('django.views.generic.list_detail',
    (r'^$', 'object_list', categ_dict, ),
    (r'^(?P<object_id>\d+)/$', 'object_detail', categ_dict, ),
    (r'^(?P<slug>[\w-]+)/$', 'object_detail', categ_dict_slug),
)

