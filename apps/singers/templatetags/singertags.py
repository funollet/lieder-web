from django.core import template
from django.models.singers import singers, VOICE_CHOICES

class SingersNode (template.Node):
    def __init__ (self, var_name):
        self.var_name = var_name
        
    def render (self, context):
        try:
            sngr= {}
            voice_keys = [v[0] for v in VOICE_CHOICES]
            for voice in voice_keys:
                sngr[voice] = [n.name for n in singers.get_list(voice__exact=voice)]
        except:
            return ''
            
        context[self.var_name] = sngr
        return ''


def do_get_singers (parser, token):
    """Returns all singers names in a dictionary, using voices as keys."""
    try:
        tag_name, arg = token.contents.split(' ', 1)
    except ValueError:
        raise template.TemplateSyntaxError, "%r tag requires an argument" % token.contents[0]
    
    if not arg[:3] == 'as ':
        raise template.TemplateSyntaxError, "%r tag had invalid arguments" % tag_name
    try:
        var_name = arg[3:]
    except IndexError:
        raise template.TemplateSyntaxError, "%r tag had invalid arguments" % tag_name
        
    return SingersNode(var_name)


register = template.Library()
register.tag ('get_singers', do_get_singers)




###########################################################

def test_render ():
    cntxt = template.Context()
    sng = SingersNode('singers').render(cntxt)
    print cntxt
    
def test_tag ():
    from pprint import pprint
    
    cntxt = template.Context()
    parser = template.Parser(None)
    token = template.Token('TOKEN_TEXT', 'get_singers as singers')
    sng = do_get_singers (parser, token).render(cntxt)
    pprint (cntxt['singers'])
    
if __name__ == '__main__':
    test_tag()