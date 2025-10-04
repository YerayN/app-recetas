from django.db import models

class Receta(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    tiempo_preparacion = models.PositiveIntegerField(help_text="Tiempo en minutos")
    instrucciones = models.TextField()
    ingredientes = models.TextField(help_text="Lista de ingredientes, uno por línea")
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
