from .models import Menu

class IndexMenus(object):
    def process_request(self, request):
        request.index_menus = Menu.objects.filter(visible=True)

