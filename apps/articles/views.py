from django.views.generic.list_detail import object_list, object_detail
from lieder.apps.misc.decorators import *


def limited_object_list (*args, **kwargs):
    return object_list (*args, **kwargs)
limited_object_list = public_objects_list (limited_object_list)
 
def limited_object_detail (*args, **kwargs):
    return object_detail (*args, **kwargs)
limited_object_detail = public_objects_detail (limited_object_detail)
    


def articles_on_section (request, queryset, object_id=None, slug=None,
        slug_field=None, *args, **kwargs):
    
    if request.user.is_anonymous() :
        # slug: section's slug
        #queryset = queryset.filter(slug=slug).get().article_set.model.public_objects.all()
        queryset = queryset.filter(status='pbl').filter(section__slug__exact=slug)
    else:
        queryset = queryset.filter(section__slug__exact=slug)
    return object_list (request, queryset, *args, **kwargs)