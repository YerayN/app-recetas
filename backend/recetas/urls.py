from rest_framework import routers
from .views import RecetaViewSet

router = routers.DefaultRouter()
router.register(r'recetas', RecetaViewSet)

urlpatterns = router.urls
