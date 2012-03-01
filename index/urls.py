from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('index.views',
    url(r'^$', 'index'),
)

