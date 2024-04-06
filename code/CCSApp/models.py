from datetime import date
from django.db import models

# Create your models here.


fecha_inicio_por_defecto = date(2024, 3, 15)
fecha_finalizacion_por_defecto = date(2025, 3, 14)


class Periodo(models.Model):
    id_periodo = models.CharField(max_length= 10, unique= True, default= '', null= False, blank= False, primary_key= True)
    fecha_inicio_periodo = models.DateField()
    fecha_final_periodo = models.DateField()

    def __str__(self):
         return self.id_periodo


class Horario(models.Model):
    MODALIDAD_CHOICES = [
        ('presencial', 'Presencial'),
        ('virtual', 'Virtual'),
        ('mixta', 'Mixta'),
    ]

    id = models.CharField(max_length = 10, unique = True, default ='', null = False, blank = False, primary_key=True)
    fecha_inicio_hora = models.DateTimeField()
    fecha_final_hora = models.DateTimeField()
    profesor = models.ForeignKey('Profesor', on_delete=models.CASCADE)
    materia = models.ForeignKey('Materia', on_delete=models.CASCADE)
    modalidad = models.CharField(max_length=20, choices=MODALIDAD_CHOICES)#
    enlace_virtual = models.URLField(blank=True, null=True)
    salon_presencial = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f'{self.fecha_inicio_hora} - {self.fecha_final_hora} - {self.profesor} - {self.materia} ({self.modalidad})'
    
class Facultad(models.Model):
    codigo_facultad = models.CharField(max_length = 10, unique = True, default ='', null = False, blank = False, primary_key=True) #cambio
    nombre_facultad = models.CharField(max_length = 255, null = False, blank = False)

    def  __str__(self):
        return self.codigo_facultad

class Programa_de_posgrado(models.Model):
    nombre_programa = models.CharField(max_length =255, unique= True,null = False, blank = False) #cambio
    codigo_programa = models.CharField(max_length = 10, unique = True, default ='', null = False, blank = False, primary_key=True) # cambio
    fecha_inicio_programa = models.DateField(default = fecha_inicio_por_defecto, null = False, blank = False)
    ESTADO_CHOICES = [
        ("Activo","Activo"),
        ("Inactivo","Inactivo")
    ]
    estado_programa = models.CharField(max_length = 50, choices = ESTADO_CHOICES, default  = 'Activo', null = False, blank = False) #cambio
    duracion_programa = models.PositiveIntegerField(default = 1, null = False, blank = False) #cambio
    facultad_programa = models.ForeignKey(Facultad, on_delete = models.CASCADE, default = '', null = False, blank = False) #cambio
    
    modalidad_programa = models.CharField(max_length = 20, choices = [('Presencial', 'Presencial'), ('Virtual', 'Virtual'), ('Mixta', 'Mixta')], default = 'Presencial', null = False, blank = False) #cambio
    def  __str__(self):
        return self.nombre_programa
    
    
class Malla_curricular(models.Model): #replantear
    nombre_malla = models.CharField(max_length =255, primary_key=True, null = False, blank = False)
    requisitos_previos = models.TextField(null=False, blank=False)
    programa_de_posgrado = models.ForeignKey(Programa_de_posgrado, on_delete=models.CASCADE, default = '', null = False, blank = False)
    def  __str__(self):
            return self.nombre_malla
    
class Materia(models.Model):
    nombre_materia = models.CharField(max_length =255, null = False, blank = False)
    codigo_materia = models.CharField(max_length = 10, unique = True, default ='', null = False, blank = False ,primary_key=True)
    creditos_materia = models.IntegerField(default = 1, null = False, blank = False)
    syllabus = models.FileField(upload_to="syllabus/", blank=True, null=True)
    nrc = models.IntegerField(null = False, blank = False)
    def  __str__(self):
        return self.codigo_materia

class Profesor(models.Model):
    nombre_profesor = models.CharField(max_length =255, null = False, blank = False)
    cedula_profesor = models.CharField(max_length = 10, unique = True, default ='', null = False, blank = False ,primary_key=True)
    especializacion_profesor = models.CharField(max_length=255, null = False, blank = False)
    correo_electronico = models.CharField(max_length=500, null = False, blank = False)
    telefono = models.IntegerField(null = False, blank = False)
    materias = models.ForeignKey(Materia, on_delete=models.CASCADE, default = '', null = False, blank = False) #necesita cambio
    def  __str__(self):
        return self.cedula_profesor
 
class Evento(models.Model):
    nombre_evento = models.CharField(max_length =255, null = False, blank = False, primary_key = True)
    fecha_inicio_evento = models.DateField(null = False, blank = False)
    fecha_finalizacion_evento = models.DateField(null = False, blank = False)
    lugar_evento = models.TextField(null = False, blank = False)
    descripcion_evento = models.TextField(null = False, blank = False)
    programa_de_posgrado_evento = models.ForeignKey(Programa_de_posgrado, on_delete=models.CASCADE, default = '', null = False, blank = False)
    def  __str__(self):
            return self.nombre_evento
    
class Actividad(models.Model):
    nombre_actividad = models.CharField(max_length = 255, null = False, blank = False, primary_key = True)
    tipo_actividad = models.CharField(max_length = 255, null = False, blank = False)
    descripcion_actividad = models.TextField(null = False, blank = False)
    duracion_en_horas= models.PositiveIntegerField(default = 1, null = False, blank = False)
    orador_actividad = models.CharField(max_length = 255, null = False, blank = False)
    evento_actividad = models.ForeignKey(Evento, on_delete=models.CASCADE, default = '', null = False, blank = False)
    def  __str__(self):
            return self.nombre_actividad
    
class Espacio(models.Model):
    espacio_codigo = models.CharField(max_length = 255, null = False, blank = False, primary_key = True)
    capacidad_espacio = models.IntegerField(default = 30, null = False, blank = False)
    disponibilidad_espacio = models.CharField(max_length = 20, choices = [('Disponible', 'Disponible'), ('No Diponible', 'No Diponible')], default = 'Disponible', null = False, blank = False)
    TIPOS_CHOICES = (
        ('Salon', 'Salon'),
        ('Auditorio', 'Auditorio'),
        ('Coliseo', 'Coliseo'),
        ('Sala de Computo', 'Sala de Computo')
    )
    tipo = models.CharField(max_length=20, choices=TIPOS_CHOICES)
    def  __str__(self):
            return self.espacio_codigo
    
class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length =255, null = False, blank = False)
    cedula = models.CharField(max_length = 10, unique = True, default ='', null = False, blank = False ,primary_key=True)
    rol = models.CharField(max_length=255,choices = [('Coordinador', 'Coordinador'),('Gestor', 'Gestor'), ('Director de programa', 'Director de programa'), ('Lider','Lider')], null = False, blank = False)
    correo_electronico = models.CharField(max_length=500, null = False, blank = False)
    telefono = models.IntegerField( null = False, blank = False)
    def  __str__(self):
        return self.cedula

class Viaticos (models.Model):
    nombre_viatico = models.CharField(max_length =255, null = False, blank = False)
    destino_del_viatico = models.CharField(max_length =255, null = False, blank = False)
    fecha_inicio_viaje= models.DateField(null = False, blank = False)
    fecha_final_viaje= models.DateField(null = False, blank = False)
    costo_de_viaje = models.DecimalField(max_digits = 10, decimal_places =2, default = 2000000, null = False, blank = False)
    invitados_viatico = models.IntegerField(default = 10, null = False, blank = False)
    evento_viatico = models.ForeignKey(Evento, on_delete=models.CASCADE, default = '', null = False, blank = False)
    estado_viatico = models.CharField(max_length=50, choices = [('En curso', 'En curso'), ('Aprobado', 'Aprobado'), ('Rechazado', 'Rechazado')], default = 'En curso', null = False, blank = False)
    def  __str__(self):
        return self.nombre_viatico
    
class Solicitud_de_servicio(models.Model):
    nombre_solicitud = models.CharField(max_length =255, null = False, blank = False)
    tipo_de_servicio = models.CharField(max_length =255, null = False, blank = False)
    solicitante = models.CharField(max_length = 50, null = False, blank = False)
    fecha_de_solicitud = models.DateField("", null = False, blank = False)
    decripcion = models.TextField(null=False, blank=False)
    estado = models.CharField(max_length=50, choices = [('En curso', 'En curso'), ('Aprobado', 'Aprobado'), ('Rechazado', 'Rechazado')], default = 'En curso', null = False, blank = False)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, default = '', null = False, blank = False)
    def  __str__(self):
        return self.nombre_solicitud
 
class Semestre(models.Model):
    nombre_semestre = models.CharField(max_length=255, null=False, blank=False)
    estado_semestre = models.BooleanField(default=True)  # Cambiar a charfield
    carreras = models.ForeignKey(Programa_de_posgrado, on_delete = models.CASCADE, default = '', null = False, blank = False)
    materias = models.ForeignKey(Materia, on_delete=models.CASCADE, default = '', null = False, blank = False)

    def __str__(self):
        return self.nombre_semestre

class Director_de_programa(models.Model):
     nombre_director= models.CharField(max_length =255, null = False, blank = False)
     numero_director = models.IntegerField(null = False, blank = False)
     correo_director = models.CharField(max_length=500, null = False, blank = False)
     foto_de_perfil = models.ImageField(upload_to= 'fotosdirectores/')

     def __str__(self):
          return self.nombre_director

    
   