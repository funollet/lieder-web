from django.conf.urls.defaults import *
from singers.models import Singer

info_dict = { 'queryset': Singer.objects.all() }

urlpatterns = patterns('django.views.generic.list_detail',
    (r'^$', 'object_list', info_dict),
)
                       
