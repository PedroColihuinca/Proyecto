from django.contrib import admin
from .models import SliderIndex,SliderGaleria,Insumos,MisionVision



class SliderIndexAdm(admin.ModelAdmin):
    list_display = ['numero','foto']
    search_fields = ['numero']
    list_per_page = 10

class SliderGaleriaAdm(admin.ModelAdmin):
    list_display = ['numero','foto']
    search_fields = ['numero']
    list_per_page = 10

class InsumosAdm(admin.ModelAdmin):
    list_display = ['nombre','precio','descripcion','stock']
    search_fields = ['nombre','descripcion']
    list_per_page = 10

class MisionVisionAdm(admin.ModelAdmin):
    list_display = ['numero','mision','vision']
    search_fields = ['numero']
    list_per_page = 10
    
# Register your models here.

admin.site.register(SliderIndex, SliderIndexAdm)
admin.site.register(SliderGaleria, SliderGaleriaAdm)
admin.site.register(Insumos, InsumosAdm)
admin.site.register(MisionVision, MisionVisionAdm)

