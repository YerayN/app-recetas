from rest_framework import serializers
from .models import Receta, Ingrediente, Unidad, IngredienteReceta


# --- Serializers base ---
class UnidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unidad
        fields = ['id', 'nombre', 'abreviatura']


class IngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = ['id', 'nombre']


# --- Ingredientes dentro de una receta ---
class IngredienteRecetaSerializer(serializers.ModelSerializer):
    # Usamos PrimaryKeyRelatedField para vincular con modelos normalizados
    ingrediente = serializers.PrimaryKeyRelatedField(
        queryset=Ingrediente.objects.all()
    )
    unidad = serializers.PrimaryKeyRelatedField(
        queryset=Unidad.objects.all()
    )

    class Meta:
        model = IngredienteReceta
        fields = ['id', 'ingrediente', 'cantidad', 'unidad']


# --- Recetas con ingredientes anidados ---
class RecetaSerializer(serializers.ModelSerializer):
    ingredientes = IngredienteRecetaSerializer(many=True)

    class Meta:
        model = Receta
        fields = [
            'id',
            'nombre',
            'descripcion',
            'tiempo_preparacion',
            'instrucciones',
            'ingredientes',
            'creado_en',
            'actualizado_en',
        ]

    def create(self, validated_data):
        ingredientes_data = validated_data.pop('ingredientes', [])
        receta = Receta.objects.create(**validated_data)
        for ingrediente in ingredientes_data:
            IngredienteReceta.objects.create(receta=receta, **ingrediente)
        return receta

    def update(self, instance, validated_data):
        ingredientes_data = validated_data.pop('ingredientes', [])
        # Actualizamos campos de la receta
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # Reemplazamos los ingredientes asociados
        instance.ingredientes.all().delete()
        for ingrediente in ingredientes_data:
            IngredienteReceta.objects.create(receta=instance, **ingrediente)
        return instance
