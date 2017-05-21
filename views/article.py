# Create your views here.

from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.dates import YearArchiveView, MonthArchiveView
from django.db.models import Count

from taggit.models import Tag

from .common import CommonContextMixin
from wbo.models.article import (
    Article,
    Category,
)


class PublishedArticlesMixin(object):
    def get_queryset(self):
        return Article.published.all()


class ArticleListView(PublishedArticlesMixin, CommonContextMixin, ListView):
    model = Article
    context_object_name = 'articles'
    template_name = 'article/index.html'


class ArticleDetailView(PublishedArticlesMixin, CommonContextMixin, DetailView):
    model = Article
    context_object_name = 'article'
    template_name = 'article/detail.html'


class CategoryListView(CommonContextMixin, ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'article/categories.html'


class FilteredArticleListMixin(CommonContextMixin):
    model = Article
    template_name = 'article/index.html'
    def get_context_data(self, **kwargs):
        context = super(FilteredArticleListMixin, self).get_context_data(
                **kwargs)
        context['articles_filtered'] = True
        return context


class CategoryArticleList(FilteredArticleListMixin, ListView):
    context_object_name = 'articles'
    template_name = 'article/index.html'
    # model = Article
    def get_queryset(self):
        self.category = get_object_or_404(Category,
                slug__iexact=self.kwargs['slug'])
        return Article.published.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super(CategoryArticleList, self).get_context_data(**kwargs)
        context['category'] = self.category
        return context


class ArticleArchiveMixin(FilteredArticleListMixin):
    context_object_name = 'articles'
    date_field = 'published_date'

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


class TagList(CommonContextMixin, ListView):
    context_object_name = 'tags'
    template_name = 'article/tags.html'

    def get_queryset(self):
        return Tag.objects.all().annotate(
                count=Count('taggit_taggeditem_items')).filter(
                count__gt=0).order_by('name')
