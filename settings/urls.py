from django.conf.urls.defaults import *
from django.conf.settings import DEBUG, LIEDER_ROOT

urlpatterns = patterns('',
    (r'^admin/', include('django.contrib.admin.urls.admin')),
    (r'^i18n/', include('django.conf.urls.i18n')),
    #
    (r'^articles/', include('lieder.apps.articles.urls')),
    (r'^concerts/', include('lieder.apps.concerts.urls')),
    (r'^documents/', include('lieder.apps.documents.urls')),
    (r'^links/', include('lieder.apps.links.urls')),
    (r'^programmes/', include('lieder.apps.programmes.urls')),
    (r'^singers/', include('lieder.apps.singers.urls')),
    #
    (r'^', include('lieder.apps.articles.urls')),
)

if DEBUG:
    urlpatterns += patterns('',
    (r'^media-lieder/(?P<path>.*)$', 'django.views.static.serve',
      {'document_root': LIEDER_ROOT + 'media-lieder/',
       'show_indexes': True, }),
)