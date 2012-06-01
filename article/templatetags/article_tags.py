from django.template import Library

from ..models import Article

register = Library()

@register.inclusion_tag('article/tags/recent_articles.html')
def get_recent_articles(number=5):
    articles = Article.published.all()[:number]
    return {'articles': articles,}

@register.inclusion_tag('article/tags/archive_articles.html')
def get_archive_articles():
    archives = Article.published.all()
    return {'archives': archives,}

