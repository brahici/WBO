# Create your views here.

from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from django.views.generic.dates import YearArchiveView, MonthArchiveView
from django.db.models import Count

from taggit.models import Tag

from .models import Article, Category

class FilteredArticleListMixin(object):
    def get_context_data(self, **kwargs):
        context = super(FilteredArticleListMixin, self).get_context_data(
                **kwargs)
        context['articles_filtered'] = True
        return context


class CategoryArticleList(FilteredArticleListMixin, ListView):
    context_object_name = 'articles'
    template_name = 'article/index.html'
    def get_queryset(self):
        self.category = get_object_or_404(Category, slug__iexact=self.kwargs['slug'])
        return Article.published.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super(CategoryArticleList, self).get_context_data(**kwargs)
        context['category'] = self.category
        return context


class CallableQuerySetMixin(object):
    queryset = None
    def get_queryset(self):
        return self.queryset()


class ArticleArchiveMixin(CallableQuerySetMixin, FilteredArticleListMixin):
    context_object_name = 'articles'
    template_name = 'article/index.html'
    date_field = 'published_date'
    queryset = Article.published.all

    def get_context_data(self, **kwargs):
        context = super(ArticleArchiveMixin, self).get_context_data(**kwargs)
        context['year'] = self.kwargs['year']
        return context

class ArticleYearArchive(ArticleArchiveMixin, FilteredArticleListMixin,
        YearArchiveView):
    make_object_list = True


class ArticleMonthArchive(ArticleArchiveMixin, FilteredArticleListMixin,
        MonthArchiveView):
    month_format = '%m'


class ArticleTag(FilteredArticleListMixin, ListView):
    context_object_name = 'articles'
    template_name = 'article/index.html'

    def get_queryset(self):
        return Article.published.filter(
                tags__slug__exact=self.kwargs['tag_slug'])

    def get_context_data(self, **kwargs):
        context = super(ArticleTag, self).get_context_data(**kwargs)
        context['tag'] = get_object_or_404(Tag, slug=self.kwargs['tag_slug'])
        return context

class TagList(ListView):
    context_object_name = 'tags'
    template_name = 'article/tags.html'

    def get_queryset(self):
        return Tag.objects.all().annotate(
                count=Count('taggit_taggeditem_items')) \
                        .filter(count__gt=0) \
                        .order_by('name')

