from django.conf.urls.defaults import *

art_dict = {'app_label': 'articles', 'module_name': 'articles', }
art_dict_slug = dict(art_dict, slug_field='slug')
section_dict = {'app_label': 'articles', 'module_name': 'sections', }
section_dict_slug = dict(section_dict, slug_field='slug')

# limited_object_list and limited_object_detail:
#   wrappers around generic views to restric to logged-in users
#   pages witch status != 'public'
#
# Not using object_id on urls: just 'slug'; k.i.s.s.
#
urlpatterns = patterns('lieder.apps.misc.views',
    (r'^$', 'limited_object_list', section_dict, ),
    #
    # Special templates for some sections.
    (r'^enregistraments/$', 'limited_object_list',
        dict(art_dict_slug, template_name='articles/enregistraments_list') ),
    # Section default template.
    (r'^(?P<slug>[\w-]+)/$', 'limited_object_detail', section_dict_slug,),
    #
    # Every article in some sections renders an specific template.
    (r'^els-components-del-cor/(?P<slug>[\w-]+)/$', 'limited_object_detail',
        dict(art_dict_slug, template_name='articles/els-components-del-cor_detail') ),
    # Article default template.
    (r'^[\w-]+/(?P<slug>[\w-]+)/$', 'limited_object_detail', art_dict_slug,),
)
