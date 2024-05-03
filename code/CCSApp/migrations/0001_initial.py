# Generated by Django 5.0.3 on 2024-05-03 00:20

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id_departamento', models.CharField(default='000', max_length=3, primary_key=True, serialize=False)),
                ('nombre_departamento', models.CharField(default='', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Director_de_programa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_director', models.CharField(max_length=255, primary_key='')),
                ('numero_director', models.IntegerField()),
                ('correo_director', models.CharField(max_length=500)),
                ('foto_de_perfil', models.ImageField(upload_to='fotosdirectores/')),
            ],
        ),
        migrations.CreateModel(
            name='Edificio',
            fields=[
                ('nombre_edificio', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('numero_espacios', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Facultad',
            fields=[
                ('codigo_facultad', models.CharField(default='', max_length=10, primary_key=True, serialize=False, unique=True)),
                ('nombre_facultad', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Periodo',
            fields=[
                ('id_periodo', models.CharField(default='', max_length=10, primary_key=True, serialize=False, unique=True)),
                ('fecha_inicio_periodo', models.DateField(default='')),
                ('fecha_final_periodo', models.DateField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('nombre_profesor', models.CharField(max_length=255)),
                ('cedula_profesor', models.CharField(default='', max_length=10, primary_key=True, serialize=False, unique=True)),
                ('especializacion_profesor', models.CharField(max_length=255)),
                ('correo_electronico', models.CharField(max_length=500)),
                ('telefono', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('nombre', models.CharField(max_length=255)),
                ('cedula', models.CharField(default='', max_length=10, primary_key=True, serialize=False, unique=True)),
                ('rol', models.CharField(max_length=255)),
                ('departamento', models.CharField(max_length=500)),
                ('correo_electronico', models.CharField(max_length=500)),
                ('telefono', models.IntegerField()),
                ('password', models.CharField(default=0, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Espacio',
            fields=[
                ('espacio_codigo', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('capacidad_espacio', models.IntegerField(default=30)),
                ('disponibilidad_espacio', models.CharField(choices=[('Disponible', 'Disponible'), ('No Diponible', 'No Diponible')], default='Disponible', max_length=20)),
                ('tipo', models.CharField(choices=[('Salon', 'Salon'), ('Auditorio', 'Auditorio'), ('Coliseo', 'Coliseo'), ('Sala de Computo', 'Sala de Computo')], max_length=20)),
                ('edificio_espacio', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='CCSApp.edificio')),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('nombre_evento', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('fecha_inicio_evento', models.DateField()),
                ('fecha_finalizacion_evento', models.DateField()),
                ('descripcion_evento', models.TextField()),
                ('lugar_evento', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='CCSApp.espacio')),
            ],
        ),
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('nombre_actividad', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('descripcion_actividad', models.TextField()),
                ('duracion_en_horas', models.PositiveIntegerField(default=1)),
                ('orador_actividad', models.CharField(max_length=255)),
                ('evento_actividad', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='CCSApp.evento')),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('nombre_materia', models.CharField(max_length=255)),
                ('codigo_materia', models.CharField(default='', max_length=10, primary_key=True, serialize=False, unique=True)),
                ('creditos_materia', models.IntegerField(default=1)),
                ('syllabus', models.FileField(blank=True, null=True, upload_to='syllabus/')),
                ('departamento', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='CCSApp.departamento')),
            ],
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id_horario', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_inicio_horario', models.DateField(default=datetime.date(2024, 3, 15))),
                ('hora_inicio_horario', models.TimeField(default=datetime.time(8, 0))),
                ('hora_final_horario', models.TimeField(default=datetime.time(10, 0))),
                ('grupo', models.CharField(choices=[('001', '001'), ('002', '002'), ('003', '003'), ('004', '004')], default='', max_length=20)),
                ('modalidad', models.CharField(choices=[('presencial', 'Presencial'), ('virtual', 'Virtual'), ('mixta', 'Mixta')], max_length=20)),
                ('enlace_virtual', models.URLField(blank=True, null=True)),
                ('salon_presencial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CCSApp.espacio')),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CCSApp.materia')),
            ],
        ),
        migrations.CreateModel(
            name='Nrc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_nrc', models.CharField(default=0, max_length=5, unique=True)),
                ('grupo', models.PositiveIntegerField(default=1)),
                ('materia_nrc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CCSApp.materia')),
                ('periodo_nrc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CCSApp.periodo')),
            ],
        ),
        migrations.CreateModel(
            name='Materia_profesor',
            fields=[
                ('id', models.CharField(default='0000000', max_length=7, primary_key=True, serialize=False)),
                ('id_nrc', models.CharField(default='00000', max_length=5)),
                ('cedula_profesor', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='CCSApp.profesor')),
            ],
        ),
        migrations.CreateModel(
            name='Programa_de_posgrado',
            fields=[
                ('nombre_programa', models.CharField(max_length=255, unique=True)),
                ('codigo_programa', models.CharField(default='', max_length=10, primary_key=True, serialize=False, unique=True)),
                ('fecha_inicio_programa', models.DateField(default=datetime.date(2024, 3, 15))),
                ('estado_programa', models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], default='Activo', max_length=50)),
                ('duracion_programa', models.PositiveIntegerField(default=1)),
                ('modalidad_programa', models.CharField(choices=[('Presencial', 'Presencial'), ('Virtual', 'Virtual'), ('Mixta', 'Mixta')], default='Presencial', max_length=20)),
                ('director_programa', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='CCSApp.director_de_programa')),
                ('facultad_programa', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='CCSApp.facultad')),
            ],
        ),
        migrations.AddField(
            model_name='evento',
            name='programa_de_posgrado_evento',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='CCSApp.programa_de_posgrado'),
        ),
        migrations.CreateModel(
            name='Semestre',
            fields=[
                ('nombre_semestre', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('estado_semestre', models.CharField(choices=[('activo', 'Activo'), ('inactivo', 'Inactivo')], default='Activo', max_length=8)),
                ('año', models.IntegerField(default='2024')),
                ('periodo', models.IntegerField(choices=[(1, '1'), (2, '2')], default='1')),
                ('programa_semestre', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='CCSApp.programa_de_posgrado')),
            ],
        ),
        migrations.CreateModel(
            name='ProgramacionAcademica',
            fields=[
                ('id_programacionAcademica', models.CharField(default=' ', max_length=36, primary_key=True, serialize=False, unique=True)),
                ('cod_banner', models.CharField(default='', max_length=20)),
                ('horas', models.FloatField(default='')),
                ('num_creditos', models.IntegerField(default='')),
                ('modalidad', models.CharField(default='', max_length=20)),
                ('grupo', models.CharField(default='', max_length=20)),
                ('tipo_de_contrato', models.CharField(default='', max_length=200)),
                ('ciudad', models.CharField(default='', max_length=200)),
                ('correo_electronico', models.CharField(default='', max_length=200)),
                ('telefono', models.CharField(default='', max_length=200)),
                ('fecha_de_clase', models.CharField(default='', max_length=200)),
                ('estado_de_contrato', models.CharField(default='', max_length=200)),
                ('fecha_elab_contrato', models.CharField(default='', max_length=200)),
                ('num_contrato', models.CharField(default='', max_length=200)),
                ('listas_mosaicos', models.CharField(default='', max_length=200)),
                ('entrega_notas', models.CharField(default='', max_length=200)),
                ('intu_canvas', models.CharField(default='', max_length=200)),
                ('tiquetes', models.CharField(default='', max_length=200)),
                ('hotel', models.CharField(default='', max_length=200)),
                ('viaticos', models.CharField(default='', max_length=200)),
                ('departamento', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='CCSApp.departamento')),
                ('docente', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='CCSApp.profesor')),
                ('horario', models.ManyToManyField(to='CCSApp.horario')),
                ('materia', models.ManyToManyField(to='CCSApp.materia')),
                ('periodo', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='CCSApp.periodo')),
                ('programa_de_posgrado', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='CCSApp.programa_de_posgrado')),
                ('semestre', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='CCSApp.semestre')),
            ],
        ),
        migrations.AddField(
            model_name='materia',
            name='semestre',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='CCSApp.semestre'),
        ),
        migrations.CreateModel(
            name='Malla_curricular',
            fields=[
                ('nombre_malla', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('requisitos_previos', models.TextField()),
                ('programa_de_posgrado', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='CCSApp.programa_de_posgrado')),
                ('semestre', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='CCSApp.semestre')),
            ],
        ),
        migrations.CreateModel(
            name='Solicitud_de_servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_solicitud', models.CharField(max_length=255)),
                ('tipo_de_servicio', models.CharField(max_length=255)),
                ('solicitante', models.CharField(max_length=50)),
                ('fecha_de_solicitud', models.DateField(verbose_name='')),
                ('decripcion', models.TextField()),
                ('estado', models.CharField(choices=[('En curso', 'En curso'), ('Aprobado', 'Aprobado'), ('Rechazado', 'Rechazado')], default='En curso', max_length=50)),
                ('evento', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='CCSApp.evento')),
            ],
        ),
    ]
