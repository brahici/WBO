from django.conf.urls.defaults import patterns, url
from django.views.generic import DetailView, ListView

from ..models import Category
from ..views import CategoryArticleList

urlpatterns = patterns('',
    url(r'^$', ListView.as_view(
            queryset=Category.objects.get_query_set,
            context_object_name='categories',
            template_name='article/categories.html')),
    url(r'^(?P<slug>[-\w]+)/$', CategoryArticleList.as_view(),
        name='category_slug_article_list_view'),
)
