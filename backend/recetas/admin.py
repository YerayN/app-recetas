from django.contrib import admin
from .models import Receta

@admin.register(Receta)
class RecetaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tiempo_preparacion', 'creado_en')
    search_fields = ('nombre',)
    list_filter = ('creado_en',)
