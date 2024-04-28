import uuid
from datetime import *
from django.db import models

fecha_inicio_por_defecto = date(2024, 3, 15)
fecha_finalizacion_por_defecto = date(2025, 3, 14)

#AL EDITAR SI VAN A PONER UNA LLAVE FORANEA ASEGURENSE QUE EL MODELO AL QUE VAN A REFERIRSE CON LA LLAVE ESTE ARRIBA DEL QUE ESTAN EDITANDO.

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

    GRUPO = [
        ('001', '001'),
        ('002', '002'),
        ('003', '003'),
        ('004', '004')
    ]

    id_horario = models.CharField(max_length = 10, unique = True, default ='', null = False, blank = False, primary_key=True)
    fecha_inicio_hora = models.DateTimeField(default= '')
    fecha_final_hora = models.DateTimeField()
    materia = models.ForeignKey('Materia', default = '', on_delete=models.CASCADE)
    grupo = models.CharField(max_length=20, default = '', choices=GRUPO)#
    modalidad = models.CharField(max_length=20, choices=MODALIDAD_CHOICES)#
    enlace_virtual = models.URLField(blank=True, null=True)
    salon_presencial = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.id_horario
    
class Facultad(models.Model):
    codigo_facultad = models.CharField(max_length = 10, unique = True, default ='', null = False, blank = False, primary_key=True) #cambio
    nombre_facultad = models.CharField(max_length = 255, null = False, blank = False, default = '') 

    def  __str__(self):
        return f"{self.codigo_facultad} - {self.nombre_facultad}"

class Director_de_programa(models.Model):
     nombre_director= models.CharField(max_length =255, null = False, blank = False, primary_key= "")
     numero_director = models.IntegerField(null = False, blank = False)
     correo_director = models.CharField(max_length=500, null = False, blank = False)
     foto_de_perfil = models.ImageField(upload_to= 'fotosdirectores/')

     def __str__(self):
          return self.nombre_director
     
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
    director_programa = models.ForeignKey(Director_de_programa, on_delete= models.CASCADE, default = "")

    def  __str__(self):
        return f"{self.codigo_programa} - {self.nombre_programa}"

class Materia(models.Model):
    nombre_materia = models.CharField(max_length =255, null = False, blank = False)
    codigo_materia = models.CharField(max_length = 10, unique = True, default ='', null = False, blank = False ,primary_key=True)
    creditos_materia = models.IntegerField(default = 1, null = False, blank = False)
    syllabus = models.FileField(upload_to="syllabus/", blank=True, null=True)
    departamento = models.CharField(max_length =255, null = False, blank = False, default= 'Universidad Icesi')
    def  __str__(self):
        return self.codigo_materia
    
    
class Nrc(models.Model):
     id_nrc = models.CharField(max_length= 5, unique= True, default= 00000, null = False)
     periodo_nrc = models.ForeignKey(Periodo, on_delete= models.CASCADE)
     grupo = models.PositiveIntegerField(default = 1, null = False, blank = False)
     materia_nrc = models.ForeignKey(Materia, on_delete= models.CASCADE)
       
class Semestre(models.Model):
    nombre_semestre = models.CharField(max_length=255, null=False, blank=False, primary_key= True)
    estado_semestre = models.CharField(max_length= 8, null= False, blank= False,  default= 'Activo', choices= [('activo', 'Activo'), ('inactivo', 'Inactivo')])  # Cambiar a charfield
    año = models.IntegerField(blank= False, null= False, default= "2024")
    periodo = models.IntegerField(choices=[(1, '1'), (2, '2')], default= "1")
    programa_semestre = models.ForeignKey(Programa_de_posgrado, on_delete=models.CASCADE, default = '', null = False, blank = False)

    def __str__(self):
        return f"{self.año}-{self.periodo}"

class Malla_curricular(models.Model): #replantear
    nombre_malla = models.CharField(max_length =255, primary_key=True, null = False, blank = False)
    requisitos_previos = models.TextField(null=False, blank=False)
    programa_de_posgrado = models.ForeignKey(Programa_de_posgrado, on_delete=models.CASCADE, default = '', null = False, blank = False)
    semestre = models.ForeignKey(Semestre, on_delete= models.CASCADE, default= '', null = False, blank = False)
    def  __str__(self):
            return self.nombre_malla
    


class Profesor(models.Model):
    nombre_profesor = models.CharField(max_length =255, null = False, blank = False)
    cedula_profesor = models.CharField(max_length = 10, unique = True, default ='', null = False, blank = False ,primary_key=True)
    especializacion_profesor = models.CharField(max_length=255, null = False, blank = False)
    correo_electronico = models.CharField(max_length=500, null = False, blank = False)
    telefono = models.IntegerField(null = False, blank = False)
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
    descripcion_actividad = models.TextField(null = False, blank = False)
    duracion_en_horas= models.PositiveIntegerField(default = 1, null = False, blank = False)
    orador_actividad = models.CharField(max_length = 255, null = False, blank = False)
    evento_actividad = models.ForeignKey(Evento, on_delete=models.CASCADE, default = '', null = False, blank = False)
    def  __str__(self):
            return self.nombre_actividad
    
class Edificio(models.Model):
    nombre_edificio = models.CharField(max_length =255, null = False, blank = False, primary_key=True)  
    numero_espacios= models.IntegerField(null = False, blank = False)
    def __str__(self):
          return self.nombre_edificio
    
class Espacio(models.Model):
    espacio_codigo = models.CharField(max_length = 255, null = False, blank = False, primary_key = True)
    capacidad_espacio = models.IntegerField(default = 30, null = False, blank = False)
    edificio_espacio = models.ForeignKey(Edificio, on_delete=models.CASCADE, default = '', null = False, blank = False)
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
    nombre = models.CharField(max_length =255, null = False, blank = False)
    cedula = models.CharField(max_length = 10, unique = True, default ='', null = False, blank = False ,primary_key=True)
    rol = models.CharField(max_length=255, null = False, blank = False)
    departamento = models.CharField(max_length=500, null = False, blank = False)
    correo_electronico = models.CharField(max_length=500, null = False, blank = False)
    telefono = models.IntegerField( null = False, blank = False)
    password = models.CharField(max_length= 30,default= 000000000, null= False, blank = False)
    def  __str__(self):
        return self.cedula 
    
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
     
class Materia_profesor(models.Model):
     id = models.CharField(max_length= 7, null = False, default= "0000000", blank= False, primary_key= True)
     cedula_profesor = models.ForeignKey(Profesor, on_delete= models.CASCADE, default= '', null= False, blank = False)
     id_nrc = models.CharField(max_length= 5, null = False, default = '00000', blank = False)

     def __str__(self):
          return self.id

class Departamento(models.Model):
     id_departamento = models.CharField(max_length= 3, null= False, default= "000", blank = False,primary_key=True)
     nombre_departamento = models.CharField(max_length= 500, null= False, default= "", blank = False)

     def  __str__ (self):
          return f"{self.id_departamento} - {self.nombre_departamento}"
     
class ProgramacionAcademica(models.Model):
     id_programacionAcademica = models.CharField(max_length= 36, unique = True, null= False, default= " ", blank= False, primary_key= True)
     programa_de_posgrado = models.ForeignKey(Programa_de_posgrado, on_delete= models.CASCADE, default= '', null= False, blank = False)
     departamento = models.ForeignKey(Departamento, on_delete= models.CASCADE,  null= False, blank= False, default = '')
     num_creditos = models.IntegerField(null = False, blank= False, default= '')
     periodo = models.ForeignKey(Periodo, on_delete= models.CASCADE,  null= False, blank= False, default = '')
     materia = models.ForeignKey(Materia, on_delete=models.CASCADE, default = '', null = False, blank = False)
     modalidad = models.CharField(max_length= 20, default = '', null = False, blank = False)
     grupo = models.CharField(max_length= 20, default = '', null = False, blank = False)
     docente = models.ForeignKey(Profesor, on_delete=models.CASCADE, default = '', null = False, blank = False)
     semestre = models.ForeignKey(Semestre, on_delete=models.CASCADE, default = '', null = False, blank = False)

     def  __str__ (self):
          return f"Programacion Academica - {self.id_programacionAcademica}"
   