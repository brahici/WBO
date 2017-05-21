# Create your views here.
from django.views.generic import TemplateView

from .common import CommonContextMixin

class AboutView(CommonContextMixin, TemplateView):
    template_name='about.html'
