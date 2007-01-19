from django import template
from lieder.apps.menus.models import Menu,MenuItem

register = template.Library()

class MenuNode (template.Node):
    def __init__ (self, menu, var_name):
        self.menu = menu
        self.var_name = var_name

    def render (self, context):
        try:
            m = Menu.objects.filter(name=self.menu).get()
        except:
            return ''
        
        context[self.var_name] = [(it.get_link(), it.name()) for it in m.menuitem_set.all()]
        return ''


import re
def do_get_menu (parser, token):
    try:
        tag_name, arg = token.contents.split(' ', 1)
    except ValueError:
        raise template.TemplateSyntaxError, "%r tag requires an argument" % token.contents[0]
    
    m = re.search(r'(.*?) as (\w+)', arg)
    if not m:
        raise template.TemplateSyntaxError, "%r tag had invalid arguments" % tag_name
    format_string, var_name = m.groups()
    
    if not (format_string[0] == format_string[-1] and format_string[0] in ('"', "'")):
        raise template.TemplateSyntaxError, "%r tag's argument should be in quotes" % tag_name
    
    return MenuNode(format_string[1:-1], var_name)

register.tag ('get_menu', do_get_menu)


#def show_menu_ul ():
    #return {'menu_ul':
        #MenuItem.objects.filter(menu__name__exact='horitzontal') }

#register.inclusion_tag('menus/menu_ul_emm.html')(show_menu_ul)





###############################################################################
# testing

def test_class_menunode():
    cntxt = {}
    m = MenuNode('horitzontal', 'menu_items')
    print m.render (cntxt)
    print
    print cntxt


def run_tests():
    test_class_menunode()


if __name__ == '__main__':
    run_tests()
