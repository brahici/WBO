from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView

from ..models import Article
from ..views import ArticleYearArchive, ArticleMonthArchive

urlpatterns = patterns('',
    url(r'^$', ListView.as_view(
            queryset=Article.published.get_query_set,
            context_object_name='articles',
            template_name='article/index.html')),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$',
            DetailView.as_view(
                model=Article,
                context_object_name='article',
                template_name='article/detail.html'),
            name='article_ymd_slug_view'),
    url(r'^(?P<pk>\d+)/$', DetailView.as_view(
            queryset=Article.published.get_query_set(),
            context_object_name='article',
            template_name='article/detail.html')),
    url(r'^(?P<slug>[-\w]+)/$', DetailView.as_view(
                queryset=Article.published.get_query_set(),
                context_object_name='article',
                template_name='article/detail.html'),
            name='article_slug_view'),
    url(r'archives/(?P<year>\d{4})/$', ArticleYearArchive.as_view(),
            name='article_archive_year'),
    url(r'archives/(?P<year>\d{4})/(?P<month>\d{2})/$',
            ArticleMonthArchive.as_view(),
            name='article_archive_month'),
)
