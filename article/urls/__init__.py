from django.conf.urls import url, include, patterns

urlpatterns = patterns('',
    url(r'^article/', include('article.urls.article')),
    url(r'^category/', include('article.urls.category')),
)

