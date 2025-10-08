from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from recetas.views import RecetaViewSet, IngredienteViewSet, UnidadViewSet, PlanSemanalViewSet
from . import views

router = DefaultRouter()
router.register(r"recetas", RecetaViewSet, basename="receta")
router.register(r"ingredientes", IngredienteViewSet, basename="ingrediente")
router.register(r"unidades", UnidadViewSet, basename="unidad")
router.register(r"plan", PlanSemanalViewSet, basename="plan")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls")),
    path('auth/csrf-cookie/', views.csrf_cookie_view, name='csrf-cookie'),
]
