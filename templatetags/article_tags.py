from django.template import Library

from taggit.models import Tag

from wbo.models.article import (
    Article,
    Category,
)

register = Library()

@register.inclusion_tag('article/tags/recent_articles.html')
def get_recent_articles(number=5):
    articles = Article.published.all()[:number]
    return {'articles': articles,}

@register.inclusion_tag('article/tags/archive_articles.html')
def get_archive_articles():
    archives = Article.published.all()
    return {'archives': archives,}

@register.inclusion_tag('article/tags/category.html')
def get_categories():
    categories = Category.objects.all()
    return {'categories': categories,}

@register.inclusion_tag('article/tags/tag.html')
def get_tags():
    tags = Tag.objects.all().order_by('name')
    return {'tags': tags,}

