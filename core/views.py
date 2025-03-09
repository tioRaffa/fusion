from django.views.generic import TemplateView
from .models import ServiceModel, TeamModel

# Create your views here.

class IndexView(TemplateView):
    template_name = 'pages/index.html'
    
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context["servico"] = ServiceModel.objects.all()
        context["team"] = TeamModel.objects.all()
        return context
    
    
class NotFoundView(TemplateView):
    template_name = "pages/404_error.html"
    
    
    