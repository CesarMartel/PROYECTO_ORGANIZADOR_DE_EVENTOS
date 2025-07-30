# myapp/models.py

from django.db import models

class Evento(models.Model):
    nombre = models.CharField(max_length=200)
    fecha = models.DateField()
    hora = models.TimeField()
    ubicacion = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50, default='presencial') 
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ['fecha', 'hora'] 
