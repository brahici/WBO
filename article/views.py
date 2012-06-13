# Create your views here.

from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from django.views.generic.dates import YearArchiveView, MonthArchiveView
from .models import Article, Category


class CategoryArticleList(ListView):
    context_object_name = 'articles'
    template_name = 'article/index.html'
    def get_queryset(self):
        category = get_object_or_404(Category, slug__iexact=self.kwargs['slug'])
        return Article.published.filter(category=category)


class CallableQuerySetMixin(object):
    queryset = None
    def get_queryset(self):
        return self.queryset()


class ArticleArchiveMixin(CallableQuerySetMixin):
    context_object_name = 'articles'
    template_name = 'article/index.html'
    date_field = 'published_date'
    queryset = Article.published.all


class ArticleYearArchive(ArticleArchiveMixin, YearArchiveView):
    make_object_list = True


class ArticleMonthArchive(ArticleArchiveMixin, MonthArchiveView):
    month_format = '%m'

