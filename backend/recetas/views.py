from rest_framework import viewsets, filters
from .models import Receta, Ingrediente, Unidad
from .serializers import RecetaSerializer, IngredienteSerializer, UnidadSerializer


class UnidadViewSet(viewsets.ModelViewSet):
    queryset = Unidad.objects.all()
    serializer_class = UnidadSerializer


class IngredienteViewSet(viewsets.ModelViewSet):
    queryset = Ingrediente.objects.all()
    serializer_class = IngredienteSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nombre']


class RecetaViewSet(viewsets.ModelViewSet):
    queryset = Receta.objects.all().order_by('-creado_en')
    serializer_class = RecetaSerializer
