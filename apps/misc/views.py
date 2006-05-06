from django.views.generic.list_detail import object_list, object_detail
from lieder.apps.misc.decorators import *


def limited_object_list (*args, **kwargs):
    return object_list (*args, **kwargs)
limited_object_list = anon_gets_public_objs (limited_object_list)
 
def limited_object_detail (*args, **kwargs):
    return object_detail (*args, **kwargs)
limited_object_detail = anon_gets_public_objs (limited_object_detail)
    
