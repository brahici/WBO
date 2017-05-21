from django.views.generic import TemplateView

from .common import CommonContextMixin

from wbo.models.article import Article

class IndexView(CommonContextMixin, TemplateView):
    template_name = 'index/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['last_article'] = Article.get_last_published()
        return context
