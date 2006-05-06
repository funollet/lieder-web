

def anon_gets_public_objs (func):
    """For non-authenticated users, restrict querys to public pages.

    Use as decorator for generic views.
    """
    
    def add_item_to_dict (request, *args, **kwargs):
        if request.user.is_anonymous() :
            kwargs.update(extra_lookup)
        return func(request, *args, **kwargs)

    extra_lookup = {'extra_lookup_kwargs': {'status__exact': 'pbl'}}

    return add_item_to_dict


