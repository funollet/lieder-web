from django import template
from lieder.apps.articles.models import Section

register = template.Library()

def show_enregistraments_list ():
    return {'section_list':
        Section.objects.filter(slug= 'enregistraments-realizats').get().article_set.all() }

register.inclusion_tag('articles/enregistraments_list_emm.html')(show_enregistraments_list)

