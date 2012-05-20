from django.conf.urls.defaults import patterns, url
from django.views.generic import DetailView, ListView

from ..models import Article

urlpatterns = patterns('',
    url(r'^$', ListView.as_view(
            queryset=Article.published.get_query_set,
            context_object_name='articles',
            template_name='article/index.html')),
    url(r'^(?P<pk>\d+)/$', DetailView.as_view(
            model=Article,
            context_object_name='article',
            template_name='article/detail.html')),
    url(r'^(?P<slug>[-\w]+)/$', DetailView.as_view(
            model=Article,
            context_object_name='article',
            template_name='article/detail.html'),
        name='article_slug_view'),
)
