from django.contrib import admin
from .models import Receta, IngredienteReceta, Ingrediente, Unidad

class IngredienteRecetaInline(admin.TabularInline):
    model = IngredienteReceta
    extra = 1

@admin.register(Receta)
class RecetaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tiempo_preparacion', 'creado_en')
    inlines = [IngredienteRecetaInline]

@admin.register(Ingrediente)
class IngredienteAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ['nombre']

@admin.register(Unidad)
class UnidadAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'abreviatura']
