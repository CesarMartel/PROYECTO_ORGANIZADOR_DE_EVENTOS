# myapp/models.py

from django.db import models

class Evento(models.Model):
    nombre = models.CharField(max_length=200)
    fecha = models.DateField()
    hora = models.TimeField()
    ubicacion = models.CharField(max_length=100) # Podríamos hacer esto un ChoiceField si la lista es fija y pequeña
    tipo = models.CharField(max_length=50, default='presencial') # 'presencial' o 'virtual'
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ['fecha', 'hora'] # Ordenar eventos por fecha y hora por defecto