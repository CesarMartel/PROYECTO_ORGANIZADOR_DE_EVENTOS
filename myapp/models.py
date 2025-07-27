from django.db import models

# Create your models here.
class project(models.Model):
    name = models.CharField(max_length=100)

class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    fecha = models.DateTimeField()
    ubicacion = models.CharField(max_length=255)
    organizador = models.CharField(max_length=100)
    descripcion = models.TextField()