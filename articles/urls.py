from django.conf.urls.defaults import *
from lieder.apps.articles.models import Article, Section

art_dict = {'queryset': Article.objects.all(), 'slug_field': 'slug'}
section_dict = {'queryset': Section.objects.all(), 'slug_field': 'slug'}

# limited_object_list and limited_object_detail:
#   wrappers around generic views to restric to logged-in users
#   pages witch status != 'public'
#
# Not using object_id on urls: just 'slug'; k.i.s.s.
#
urlpatterns = patterns('lieder.apps.articles.views',
    #(r'^$', 'limited_object_list', section_dict, ),
    (r'^$', 'limited_object_detail', 
        dict(art_dict, slug='inici', template_name='articles/inici_detail.html') ),
    #
    # Special templates for some sections.
    (r'^(?P<slug>enregistraments-realizats)/$', 'articles_on_section',
        dict(art_dict, template_name='articles/enregistraments_list.html', ) ),
    (r'^(?P<slug>la-premsa-ha-dit)/$', 'articles_on_section',
        dict(art_dict, template_name='articles/premsa.html',) ),
    # Section default template.
    (r'^(?P<slug>[\w-]+)/$', 'articles_on_section', art_dict,),
    #
    # Every article in some sections renders an specific template.
    (r'^els-components-del-cor/(?P<slug>[\w-]+)/$', 'limited_object_detail',
        dict(art_dict, template_name='articles/els-components-del-cor_detail.html') ),
    (r'^enregistraments-realizats/(?P<slug>[\w-]+)/$', 'limited_object_detail',
        dict(art_dict, template_name='articles/enregistraments_detail.html') ),
    # Article default template.
    (r'^[\w-]+/(?P<slug>[\w-]+)/$', 'limited_object_detail', art_dict,),
)
