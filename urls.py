from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from wbo import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wbo.views.home', name='home'),
    # url(r'^wbo/', include('wbo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^voppos/', include(admin.site.urls)),

    # index
    url(r'^$', include('wbo.index.urls')),

    # article
    url(r'', include('wbo.article.urls')),

    # about
    url(r'^about/', include('wbo.about.urls')),
)

if settings.DEBUG:
    # static content in debug environment
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
    )

