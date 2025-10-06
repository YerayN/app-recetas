from rest_framework import routers
from .views import RecetaViewSet, IngredienteViewSet, UnidadViewSet

router = routers.DefaultRouter()
router.register(r'recetas', RecetaViewSet)
router.register(r'ingredientes', IngredienteViewSet)
router.register(r'unidades', UnidadViewSet)

urlpatterns = router.urls
