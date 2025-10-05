from django.db import models

class Receta(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    tiempo_preparacion = models.PositiveIntegerField(help_text="Tiempo en minutos")
    instrucciones = models.TextField()
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre


class IngredienteReceta(models.Model):
    receta = models.ForeignKey(
        Receta,
        related_name="ingredientes",
        on_delete=models.CASCADE
    )
    nombre = models.CharField(max_length=100)
    cantidad = models.FloatField(null=True, blank=True)
    unidad = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.cantidad or ''} {self.unidad or ''} {self.nombre}".strip()
