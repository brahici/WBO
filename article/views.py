# Create your views here.

from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from .models import Article, Category


class CategoryArticleList(ListView):
    context_object_name = 'articles'
    template_name = 'article/index.html'

    def get_queryset(self):
        category = get_object_or_404(Category, slug__iexact=self.kwargs['slug'])
        return Article.published.filter(category=category)

