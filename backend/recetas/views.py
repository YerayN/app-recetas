from rest_framework import viewsets
from .models import Receta
from .serializers import RecetaSerializer

class RecetaViewSet(viewsets.ModelViewSet):
    queryset = Receta.objects.all().order_by('-creado_en')
    serializer_class = RecetaSerializer
