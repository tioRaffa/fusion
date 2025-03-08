from django.db import models
from django.contrib.auth.models import User

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
        ('ni-users', 'users'),
        ('lni-layers', 'design'),
        ('lni-mobile', 'mobile'),
        ('lni-rocket', 'rocket'),
    )
    
    service = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    icon = models.CharField(max_length=12, choices=ICON_CHOICES)
    
    def __str__(self):
        return self.service
    
    
class TeamModel(Base):
    
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    service = models.ForeignKey(ServiceModel, on_delete=models.SET_NULL, null=True)
    pic_profile = models.ImageField(upload_to='fusion/media/%y/%m/%d', blank=True, null=True)
    facebook = models.CharField(max_length=100, default='#')
    twitter = models.CharField(max_length=100, default='#')
    instagram = models.CharField(max_length=100, default='#')
    
    def __str__(self):
        return self.user.first_name
    
    