from django.contrib import admin
from .models import ServiceModel, TeamModel, CargoModel, FeaturesModel, PostModel, ChassiModel, CarModel

# Register your models here.

@admin.register(ServiceModel)
class ServiceModelAdmin(admin.ModelAdmin):
    list_display = ['service']
    ordering = ['-id']
    
    
@admin.register(CargoModel)
class CargoModelAdmin(admin.ModelAdmin):
    list_display = ['service']
    ordering = ['-id']
    
    
@admin.register(TeamModel)
class TeamModelAdmin(admin.ModelAdmin):
    list_display = ['id','user', 'service', 'active']  
    list_display_links = ['id', 'user']  
    list_editable = ['active']  
    ordering = ['-id']
    

@admin.register(FeaturesModel)
class FeaturesModelAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'features'
    ]
    list_display_links = ['id', 'features']
    ordering = ['-id']
    
    
@admin.register(PostModel)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'title']
    list_display_links = ['id', 'user']
    ordering = ['-id']
    
    
@admin.register(ChassiModel)
class ChassiModelAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'numero'
    ]
    
@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'car_brand', 'car_model', 'chassi', 'price'
    ]
    list_display_links = [
        'id', 'car_brand', 'car_model'
    ]
    ordering = [
        '-id'
    ]