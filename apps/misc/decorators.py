

def public_objects_detail (func):
    """For non-authenticated users, restrict querys to public pages.

    Use as decorator for generic views.
    """
    
    def filter_public_objects (request, queryset, *args, **kwargs):
        if request.user.is_anonymous() :
            queryset = queryset.model.public_objects
        return func(request, queryset, *args, **kwargs)

    return filter_public_objects



def public_objects_list (func):
    """For non-authenticated users, restrict querys to public pages.

    Use as decorator for generic views.
    """
    
    def filter_public_objects (request, queryset, *args, **kwargs):
        if request.user.is_anonymous() :
            newqueryset = queryset.get().article_set.filter(status='pbl')
        return func(request, queryset, *args, **kwargs)

    return filter_public_objects


