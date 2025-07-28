from django.db import models

# Create your models here.
class RegistroEventos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    fecha = models.DateTimeField()
    ubicacion = models.CharField(max_length=255)
    organizador = models.CharField(max_length=100)  
    descripcion = models.TextField(verbose_name='Descripción',null=True)