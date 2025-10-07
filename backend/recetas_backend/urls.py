from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from recetas.views import (
    RecetaViewSet,
    IngredienteViewSet,
    UnidadViewSet,
    PlanSemanalViewSet,
    register,
    login_view,
    logout_view,
)

router = DefaultRouter()
router.register(r"recetas", RecetaViewSet, basename="receta")
router.register(r"ingredientes", IngredienteViewSet, basename="ingrediente")
router.register(r"unidades", UnidadViewSet, basename="unidad")
router.register(r"plan", PlanSemanalViewSet, basename="plan")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls")),

    # 👇 Endpoints personalizados
    path("api/register/", register),
    path("api/login/", login_view),
    path("api/logout/", logout_view),
]
