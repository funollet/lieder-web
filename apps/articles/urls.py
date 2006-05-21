from django.conf.urls.defaults import *

art_dict = {'app_label': 'articles', 'module_name': 'articles', 'slug_field': 'slug'}
section_dict = {'app_label': 'articles', 'module_name': 'sections', 'slug_field': 'slug'}

# limited_object_list and limited_object_detail:
#   wrappers around generic views to restric to logged-in users
#   pages witch status != 'public'
#
# Not using object_id on urls: just 'slug'; k.i.s.s.
#
urlpatterns = patterns('lieder.apps.misc.views',
    #(r'^$', 'limited_object_list', section_dict, ),
    (r'^$', 'limited_object_detail', dict(art_dict, slug='inici', template_name='articles/inici_detail') ),
    #
    # Special templates for some sections.
    (r'^enregistraments-realizats/$', 'limited_object_detail',
        dict(section_dict, template_name='articles/enregistraments_list', slug='enregistraments-realizats') ),
    (r'^la-direccio/$', 'limited_object_detail',
        dict(section_dict, template_name='articles/la-direccio', slug='la-direccio') ),
    (r'^la-premsa-ha-dit/$', 'limited_object_detail',
        dict(section_dict, template_name='articles/premsa', slug='la-premsa-ha-dit') ),
    # Section default template.
    (r'^(?P<slug>[\w-]+)/$', 'limited_object_detail', section_dict,),
    #
    # Every article in some sections renders an specific template.
    (r'^els-components-del-cor/(?P<slug>[\w-]+)/$', 'limited_object_detail',
        dict(art_dict, template_name='articles/els-components-del-cor_detail') ),
    # Article default template.
    (r'^[\w-]+/(?P<slug>[\w-]+)/$', 'limited_object_detail', art_dict,),
)
