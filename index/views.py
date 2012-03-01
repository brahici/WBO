from django.shortcuts import render_to_response
from django.template.context import RequestContext
from .models import Menu

def index(request):
    return render_to_response('index/index.html',
            context_instance=RequestContext(request))

