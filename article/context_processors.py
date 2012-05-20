from .models import Article

def article_last(request):
    return {'last_article': Article.get_last_published()}


