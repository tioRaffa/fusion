from django.views.generic import TemplateView

# Create your views here.

class IndexView(TemplateView):
    template_name = 'pages/index.html'
    
class NotFoundView(TemplateView):
    template_name = "pages/404_error.html"