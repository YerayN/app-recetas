from rest_framework import viewsets, filters, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Receta, Ingrediente, Unidad, PlanSemanal
from .serializers import RecetaSerializer, IngredienteSerializer, UnidadSerializer, PlanSemanalSerializer

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


# ------------------- VISTAS CRUD PRINCIPALES -------------------

class UnidadViewSet(viewsets.ModelViewSet):
    """CRUD completo para Unidades"""
    queryset = Unidad.objects.all()
    serializer_class = UnidadSerializer
    permission_classes = [permissions.IsAuthenticated]


class IngredienteViewSet(viewsets.ModelViewSet):
    """CRUD completo para Ingredientes"""
    queryset = Ingrediente.objects.all()
    serializer_class = IngredienteSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ["nombre"]


@method_decorator(csrf_exempt, name='dispatch')
class RecetaViewSet(viewsets.ModelViewSet):
    """CRUD para Recetas del hogar actual"""
    queryset = Receta.objects.all()
    serializer_class = RecetaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        perfil = getattr(user, "perfil", None)

        if not user.is_authenticated:
            return Receta.objects.none()

        if not perfil or not getattr(perfil, "hogar", None):
            print("⚠️ Usuario sin perfil o sin hogar asociado:", user)
            return Receta.objects.none()

        print("✅ Devolviendo recetas del hogar:", perfil.hogar)
        return Receta.objects.filter(hogar=perfil.hogar).order_by("-creado_en")

    def perform_create(self, serializer):
        user = self.request.user
        perfil = getattr(user, "perfil", None)
        if not perfil or not perfil.hogar:
            raise ValueError("El usuario no pertenece a ningún hogar válido.")
        serializer.save(hogar=perfil.hogar)


@method_decorator(csrf_exempt, name='dispatch')
class PlanSemanalViewSet(viewsets.ModelViewSet):
    """CRUD para el Plan Semanal, filtrado por hogar del usuario"""
    queryset = PlanSemanal.objects.all()
    serializer_class = PlanSemanalSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if not user.is_authenticated:
            return PlanSemanal.objects.none()
        perfil = getattr(user, "perfil", None)
        if perfil is None or perfil.hogar is None:
            return PlanSemanal.objects.none()
        return (
            PlanSemanal.objects.filter(hogar=perfil.hogar)
            .select_related("receta")
            .order_by("dia")
        )

    def perform_create(self, serializer):
        user = self.request.user
        perfil = getattr(user, "perfil", None)
        if perfil is None or perfil.hogar is None:
            raise ValueError("El usuario no pertenece a ningún hogar válido.")
        serializer.save(hogar=perfil.hogar, creado_por=user)


# ------------------- AUTENTICACIÓN -------------------

@csrf_exempt
@api_view(["POST"])
@permission_classes([AllowAny])
def register(request):
    """Registro de usuarios con creación automática de hogar y perfil."""
    username = request.data.get("username")
    password = request.data.get("password")

    if not username or not password:
        return Response({"error": "Faltan campos obligatorios."},
                        status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(username=username).exists():
        return Response({"error": "El usuario ya existe."},
                        status=status.HTTP_400_BAD_REQUEST)

    User.objects.create_user(username=username, password=password)
    return Response({"message": "Usuario creado correctamente."},
                    status=status.HTTP_201_CREATED)


@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    """Login API (para frontend con fetch)."""
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return Response({'message': 'Login correcto'}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Usuario o contraseña incorrectos'},
                        status=status.HTTP_401_UNAUTHORIZED)


@csrf_exempt
@api_view(['POST'])
def logout_view(request):
    """Logout API — cierra sesión."""
    logout(request)
    return Response({'message': 'Logout correcto'}, status=status.HTTP_200_OK)
