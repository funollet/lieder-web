from django.template import Library, Node, resolve_variable

register = Library()

class IfStartsWithNode(Node):
    def __init__(self, var1, var2, nodelist_true, nodelist_false, negate):
        self.var1, self.var2 = var1, var2
        self.nodelist_true, self.nodelist_false = nodelist_true, nodelist_false
        self.negate = negate

    def __repr__(self):
        return "<IfStartsWithNode>"

    def render(self, context):
        val1 = resolve_variable(self.var1, context)
        val2 = resolve_variable(self.var2, context)
        if (self.negate and not val1.startswith(val2)) or (not self.negate and val1.startswith(val2)):
            return self.nodelist_true.render(context)
        return self.nodelist_false.render(context)
    

def do_ifstartswith (parser, token, negate):
    """
    Output the contents of the block if the first argument begins with the second one.

    Examples::

        {% ifstartswith request.path item.get_absolute_url %}
            ...
        {% endifequal %}
    """
    bits = list(token.split_contents())
    if len(bits) != 3:
        raise TemplateSyntaxError, "%r takes two arguments" % bits[0]
    end_tag = 'end' + bits[0]
    nodelist_true = parser.parse(('else', end_tag))
    token = parser.next_token()
    if token.contents == 'else':
        nodelist_false = parser.parse((end_tag,))
        parser.delete_first_token()
    else:
        nodelist_false = NodeList()
    return IfStartsWithNode(bits[1], bits[2], nodelist_true, nodelist_false, negate)

#@register.tag
def ifstartswith(parser, token):
    return do_ifstartswith(parser, token, False)
ifstartswith = register.tag(ifstartswith)

