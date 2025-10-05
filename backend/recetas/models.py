from django.db import models

class Unidad(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    abreviatura = models.CharField(max_length=10, blank=True)

    class Meta:
        verbose_name = "Unidad"
        verbose_name_plural = "Unidades"

    def __str__(self):
        return self.abreviatura or self.nombre


class Ingrediente(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre


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
    receta = models.ForeignKey(Receta, related_name="ingredientes", on_delete=models.CASCADE)
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.PROTECT)
    cantidad = models.FloatField(null=True, blank=True)
    unidad = models.ForeignKey(Unidad, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return f"{self.cantidad or ''} {self.unidad or ''} {self.ingrediente}".strip()
