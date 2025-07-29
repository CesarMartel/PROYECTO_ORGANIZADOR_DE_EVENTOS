
from django.db import models

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    fecha = models.DateField()
    hora = models.TimeField()
    ubicacion = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20)
    descripcion = models.TextField()

    def __str__(self):
        return self.titulo
