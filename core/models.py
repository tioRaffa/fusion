from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Base(models.Model):
    create = models.DateField(auto_now_add=True)
    update = models.DateField(auto_now=True)
    active = models.BooleanField(default=True)
    
    class Meta:
        abstract = True
        
        
        
class ServiceModel(Base):
    ICON_CHOICES = (
        ('lni-cog', 'engrenagem'),
        ('lni-stats-up', 'grafico'),
        ('lni-users', 'users'),
        ('lni-layers', 'design'),
        ('lni-mobile', 'mobile'),
        ('lni-rocket', 'rocket'),
    )
    
    service = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    icon = models.CharField(max_length=12, choices=ICON_CHOICES)
    
    def __str__(self):
        return self.service
    
    
class CargoModel(Base):
    SERVICE_CHOICES = (
        ('Front-end Developer', 'Front-end Developer'),
        ('Back-end Developer', 'Back-end Developer'),
        ('Front-end Developer', 'Front-end Developer'),
        ('Designer de Produto', 'Designer de Produto'),
        ('Designer Lider', 'Designer Lider'),
    )
    
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    
    def __str__(self):
        return self.service

class TeamModel(Base):
    
    
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    service = models.ForeignKey(CargoModel, on_delete=models.SET_NULL, null=True)
    pic_profile = models.ImageField(upload_to='fusion/media/%y/%m/%d', blank=True, null=True)
    bio = models.CharField(max_length=150, default='Sem Biografia')
    facebook = models.CharField(max_length=100, default='#')
    twitter = models.CharField(max_length=100, default='#')
    instagram = models.URLField(max_length=100, default='#')
    
    def __str__(self):
        return self.user.first_name
    

class FeaturesModel(Base):
    ICON_CHOICES  = (
        ('lni-rocket', 'rocket'),
        ('lni-laptop-phone', 'laptop e celular'),
        ('lni-cog', 'engrenagem'),
        ('lni-leaf', 'folha'),
        ('lni-layers', 'camadas'),
    )
    features = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    icon = models.CharField(choices=ICON_CHOICES)
    
    
class PostModel(Base):
    user = models.ForeignKey(User, verbose_name=_("usuario"), on_delete=models.CASCADE)
    title = models.CharField(_("Titulo"), max_length=50)
    text = models.TextField(_("Texto"))
    
    def __str__(self):
        return self.title