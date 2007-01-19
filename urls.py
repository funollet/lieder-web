from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('',
    (r'^admin/', include('django.contrib.admin.urls')),
    (r'^i18n/', include('django.conf.urls.i18n')),
    (r'^r/', include('django.conf.urls.shortcut')),
    #
    #(r'^articles/', include('articles.urls')),
    (r'^concerts/', include('concerts.urls')),
    (r'^documents/', include('documents.urls')),
    (r'^links/', include('links.urls')),
    (r'^programmes/', include('programmes.urls')),
    (r'^singers/', include('singers.urls')),
    #(r'^stockphoto/', include('stockphoto.urls')),
    #
    (r'^', include('articles.urls')),
)

if settings.LOCAL_DEV:
    urlpatterns = patterns('',
    (r'^media-lieder/(?P<path>.*)$', 'django.views.static.serve',
      {'document_root': settings.MEDIA_ROOT,
       'show_indexes': True, }),
) + urlpatterns