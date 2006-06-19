

def anon_gets_public_objs (func):
    """For non-authenticated users, restrict querys to public pages.

    Use as decorator for generic views.
    """
    
    def add_item_to_dict (request, queryset, *args, **kwargs):
        if request.user.is_anonymous() :
            newqueryset = queryset.filter(status='pbl')
        else:
            newqueryset = queryset
            
        return func(request, newqueryset, *args, **kwargs)

    return add_item_to_dict


