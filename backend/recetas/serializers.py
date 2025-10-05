from rest_framework import serializers
from .models import Receta, IngredienteReceta

class IngredienteRecetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = IngredienteReceta
        fields = ['id', 'nombre', 'cantidad', 'unidad']

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
            'actualizado_en'
        ]

    def create(self, validated_data):
        ingredientes_data = validated_data.pop('ingredientes', [])
        receta = Receta.objects.create(**validated_data)
        for ingrediente in ingredientes_data:
            IngredienteReceta.objects.create(receta=receta, **ingrediente)
        return receta

    def update(self, instance, validated_data):
        ingredientes_data = validated_data.pop('ingredientes', [])
        # Actualizamos los campos de la receta
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # Borramos los ingredientes antiguos y creamos los nuevos
        instance.ingredientes.all().delete()
        for ingrediente in ingredientes_data:
            IngredienteReceta.objects.create(receta=instance, **ingrediente)
        return instance
