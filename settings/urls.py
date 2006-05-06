from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^admin/', include('django.contrib.admin.urls.admin')),
    (r'^i18n/', include('django.conf.urls.i18n')),
    (r'^lieder-media/(?P<path>.*)$', 'django.views.static.serve',
      {'document_root': '/home/jordif/devel/djangos/lieder/media/',
       'show_indexes': True, }),
    #
    (r'^articles/', include('lieder.apps.articles.urls')),
    (r'^concerts/', include('lieder.apps.concerts.urls')),
    (r'^documents/', include('lieder.apps.documents.urls')),
    (r'^links/', include('lieder.apps.links.urls')),
    (r'^programmes/', include('lieder.apps.programmes.urls')),
    (r'^singers/', include('lieder.apps.singers.urls')),
    #
    #(r'^texts/', include('lieder.text_store.urls')),
    #(r'^/', include('lieder.text_store.urls')),
    (r'^', include('lieder.apps.links.urls')),
)
