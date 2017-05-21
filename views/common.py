# from django.contrib.sites.models import Site

from wbo.models.index import Menu

class CommonContextMixin(object):
    def get_context_data(self, **kwargs):
        context = super(CommonContextMixin, self).get_context_data(**kwargs)
        # context['site'] = Site.objects.get_current()
        context['index_menus'] = Menu.objects.filter(visible=True)
        return context
