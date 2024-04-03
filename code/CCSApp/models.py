from datetime import date
from django.db import models

fecha_inicio_por_defecto = date(2024, 3, 15)
fecha_finalizacion_por_defecto = date(2025, 3, 14)

# Create your models here.

class Horario(models.Model):
    MODALIDAD_CHOICES = [
        ('presencial', 'Presencial'),
        ('virtual', 'Virtual'),
        ('mixta', 'Mixta'),
    ]

    id_horario = models.AutoField(primary_key=True)
    fecha_inicio_horario = models.DateTimeField() #cambio
    fecha_final_horario = models.DateTimeField() #cambio
    profesor_asignado_horario = models.ForeignKey('Profesor', on_delete=models.CASCADE)
    materia_horario = models.ForeignKey('Materia', on_delete=models.CASCADE)
    modalidad = models.CharField(max_length=20, choices=MODALIDAD_CHOICES) #Modalidad amarrada a la propia modalidad del programa - LLAVE FORANEA
    enlace_virtual = models.URLField(blank=True, null=True)
    salon_presencial = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f'{self.fecha_hora} - {self.profesor} - {self.materia} ({self.modalidad})' #necesita cambio
    
class Facultad(models.Model):
    codigo_facultad = models.CharField(max_length = 10, unique = True, default ='', null = False, blank = False, primary_key=True) #cambio
    nombre_facultad = models.CharField(max_length = 255, null = False, blank = False, primary_key=True)

    def  __str__(self):
        return self.codigo_facultad

class Programa_de_posgrado(models.Model):
    nombre_programa = models.CharField(max_length =255, unique= True,null = False, blank = False) #cambio
    codigo_programa = models.CharField(max_length = 10, unique = True, default ='', null = False, blank = False, primary_key=True) # cambio
    # descripcion = models.TextField(null=False, blank=False)
    fecha_inicio_programa = models.DateField(default = fecha_inicio_por_defecto, null = False, blank = False)
    #fecha_finalizacion_programa = models.DateField(default = fecha_finalizacion_por_defecto, null = False, blank = False) #cambio
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
    syllabus_materia = models.FieldFile(upload_to='Documentos/') #cambio
    nrc = models.IntegerField(max_length = 6, null = False, blank = False)
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
    nombre = models.CharField(max_length =255, null = False, blank = False, primary_key = True)
    fecha_inicio = models.DateField(null = False, blank = False)
    fecha_finalizacion = models.DateField(null = False, blank = False)
    lugar = models.TextField(null = False, blank = False)
    descripcion = models.TextField(null = False, blank = False)
    programa_de_posgrado = models.ForeignKey(Programa_de_posgrado, on_delete=models.CASCADE, default = '', null = False, blank = False)
    def  __str__(self):
            return self.nombre
    
class Actividad(models.Model):
    nombre = models.CharField(max_length = 255, null = False, blank = False, primary_key = True)
    tipo = models.CharField(max_length = 255, null = False, blank = False)
    descripcion = models.TextField(null = False, blank = False)
    duracion_H= models.PositiveIntegerField(default = 1, null = False, blank = False)
    orador = models.CharField(max_length = 255, null = False, blank = False)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, default = '', null = False, blank = False)
    def  __str__(self):
            return self.nombre
    
class Espacio(models.Model):
    espacio_codigo = models.CharField(max_length = 255, null = False, blank = False, primary_key = True)
    capacidad = models.IntegerField(default = 30, null = False, blank = False)
    disponibilidad = models.CharField(max_length = 20, choices = [('Disponible', 'Disponible'), ('No Diponible', 'No Diponible')], default = 'Disponible', null = False, blank = False)
    TIPOS_CHOICES = (
        ('salon', 'salon'),
        ('auditorio', 'auditorio'),
        ('coliseo', 'coliseo'),
        ('sala computo', 'sala computo')
    )
    tipo = models.CharField(max_length=20, choices=TIPOS_CHOICES)
    def  __str__(self):
            return self.espacio_codigo
    
class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length =255, null = False, blank = False)
    cedula = models.CharField(max_length = 10, unique = True, default ='', null = False, blank = False ,primary_key=True)
    rol = models.CharField(max_length=255,choices = [('Coordinador', 'Coordinador'), ('Director de programa', 'Director de programa'), ('Lider','Lider')], null = False, blank = False)
    # departamento = models.CharField(max_length=500, null = False, blank = False)
    correo_electronico = models.CharField(max_length=500, null = False, blank = False)
    telefono = models.IntegerField( null = False, blank = False)
    def  __str__(self):
        return self.cedula

class Viaticos (models.Model):
    nombre = models.CharField(max_length =255, null = False, blank = False)
    destino = models.CharField(max_length =255, null = False, blank = False)
    fecha_viaje = models.DateField(null = False, blank = False)
    costo_de_viaje = models.DecimalField(max_digits = 10, decimal_places =2, default = 2000000, null = False, blank = False)
    invitados = models.IntegerField(default = 10, null = False, blank = False)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, default = '', null = False, blank = False)
    estado = models.CharField(max_length=50, choices = [('En curso', 'En curso'), ('Aprobado', 'Aprovado'), ('Rechazado', 'Rechazado')], default = 'En curso', null = False, blank = False)
    def  __str__(self):
        return self.nombre
    
class Solicitud_de_servicio(models.Model):
    nombre_solicitud = models.CharField(max_length =255, null = False, blank = False)
    tipo_de_servicio = models.CharField(max_length =255, null = False, blank = False)
    solicitante = models.CharField(max_length = 50, null = False, blank = False)
    fecha_de_solicitud = models.DateField("", null = False, blank = False)
    decripcion = models.TextField(null=False, blank=False)
    estado = models.CharField(max_length=50, choices = [('En curso', 'En curso'), ('Aprobado', 'Aprovado'), ('Rechazado', 'Rechazado')], default = 'En curso', null = False, blank = False)
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

    
   