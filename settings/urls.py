from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('',
    (r'^admin/', include('django.contrib.admin.urls')),
    (r'^i18n/', include('django.conf.urls.i18n')),
    (r'^r/', include('django.conf.urls.shortcut')),
    #
    #(r'^articles/', include('lieder.apps.articles.urls')),
    (r'^concerts/', include('lieder.apps.concerts.urls')),
    (r'^documents/', include('lieder.apps.documents.urls')),
    (r'^links/', include('lieder.apps.links.urls')),
    (r'^programmes/', include('lieder.apps.programmes.urls')),
    (r'^singers/', include('lieder.apps.singers.urls')),
    #(r'^stockphoto/', include('lieder.apps.stockphoto.urls')),
    #
    (r'^', include('lieder.apps.articles.urls')),
)

if settings.LOCAL_DEV:
    urlpatterns = patterns('',
    (r'^media-lieder/(?P<path>.*)$', 'django.views.static.serve',
      {'document_root': settings.MEDIA_ROOT,
       'show_indexes': True, }),
) + urlpatterns