from datetime import date
from django.db import models

fecha_inicio_por_defecto = date(2024, 3, 15)
fecha_finalizacion_por_defecto = date(2025, 3, 14)

# Create your models here.
class Facultad(models.Model):
    nombre = models.CharField(max_length = 255)
    descripcion = models.TextField()

    def  __str__(self):
        return self.nombre

class Carrera_de_posgrado(models.Model):
    name = models.CharField(max_length =255)
    codigo = models.CharField(max_length = 10, unique = True, default ='')
    descripcion = models.TextField()
    fecha_inicio = models.DateField(default = fecha_inicio_por_defecto)
    fecha_finalizacion = models.DateField(default = fecha_finalizacion_por_defecto)
    value = models.DecimalField(max_digits = 10, decimal_places =2, default = 2000000)
    duracion = models.PositiveIntegerField(default = 1)
    facultad= models.ForeignKey(Facultad, on_delete = models.CASCADE, default = '')
    modalidad = models.CharField(max_length = 20, choices = [('Presencial', 'Presencial'), ('Virtual', 'Virtual')], default = 'Presencial')

    def  __str__(self):
        return self.name
    
