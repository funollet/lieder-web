"""Custom views for Concert objects."""

from django.views.generic.list_detail import object_list
from datetime import datetime

def futureitems_object_list (request, queryset, *args, **kwargs):
    """Calls the generic view but only shows items with pub_date in future."""
    queryset = queryset.filter( pub_date__gt=str(datetime.now()) )
    return object_list (request, queryset, *args, **kwargs)