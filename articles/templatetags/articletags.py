from django import template
from articles.models import Section

register = template.Library()

def show_enregistraments_list ():
    return {'enreg_list':
        Section.objects.filter(slug= 'enregistraments-realizats').get().article_set.all() }

register.inclusion_tag('articles/enregistraments_emm_table.html')(show_enregistraments_list)

