from django.views.generic import TemplateView, FormView
from .models import ServiceModel, TeamModel, FeaturesModel
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import ContactForm

# Create your views here.

class IndexView(FormView):
    template_name = 'pages/index.html'
    form_class = ContactForm
    success_url = reverse_lazy('fusion:home')

    
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context["servico"] = ServiceModel.objects.order_by('?').all()
        context["team"] = TeamModel.objects.order_by('?').all()
        context["features"] = FeaturesModel.objects.all()
        context["form"] = self.get_form()
        
        return context
    
    def form_valid(self, form, *args, **kwargs):
        form.send_email()
        messages.success(self.request, 'E-mail enviado com sucesso!')
        
        return super(IndexView, self).form_valid(form, *args, **kwargs)
    
    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enviar o E-mail!')
        
        response = super(IndexView, self).form_invalid(form, *args, **kwargs)
        return response
    
    
    
class NotFoundView(TemplateView):
    template_name = "pages/404_error.html"
    
    
    