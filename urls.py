from django.conf.urls import url

from .views import (
    index,
    about,
    article,
)


app_name = 'wbo'
urlpatterns = [
    url(r'^$', index.IndexView.as_view(), name='index'),
    url(r'about/$', about.AboutView.as_view(), name='about'),
    url(r'article/$', article.ArticleListView.as_view()),

    url(r'article/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$',
            article.ArticleDetailView.as_view(),
            name='article_ymd_slug_view'),
    url(r'article/(?P<pk>\d+)/$', article.ArticleDetailView.as_view(),
            name='article_pk_view'),
    url(r'article/(?P<slug>[-\w]+)/$', article.ArticleDetailView.as_view(),
            name='article_slug_view'),
    url(r'article/archives/(?P<year>\d{4})/$', article.ArticleYearArchive.as_view(),
            name='article_archive_year'),
    url(r'article/archives/(?P<year>\d{4})/(?P<month>\d{2})/$',
            article.ArticleMonthArchive.as_view(),
            name='article_archive_month'),
    url(r'category/$', article.CategoryListView.as_view(),
            name='category_view'),
    url(r'category/(?P<slug>[-\w]+)/$', article.CategoryArticleList.as_view(),
            name='category_slug_article_list_view'),
    url(r'tag/$', article.TagList.as_view(), name='tag_view'),
    url(r'tag/(?P<tag_slug>[-\w]+)/$', article.ArticleTag.as_view(),
            name='articles_by_tag'),
]
