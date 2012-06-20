from django.conf.urls.defaults import patterns, url
from django.views.generic import ListView

from taggit.models import Tag

from ..views import ArticleTag, TagList

urlpatterns = patterns('',
        url(r'^$', TagList.as_view()),
        url(r'^(?P<tag_slug>[-\w]+)/$', ArticleTag.as_view(),
                name='articles_by_tag'),
)
