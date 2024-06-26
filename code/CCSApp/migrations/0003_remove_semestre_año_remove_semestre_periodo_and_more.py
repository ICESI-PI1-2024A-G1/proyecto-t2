# Generated by Django 5.0.3 on 2024-05-09 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CCSApp', '0002_rename_programa_de_posgrado_materia_programa_de_posgrado_materia'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='semestre',
            name='año',
        ),
        migrations.RemoveField(
            model_name='semestre',
            name='periodo',
        ),
        migrations.RemoveField(
            model_name='semestre',
            name='programa_semestre',
        ),
        migrations.AlterField(
            model_name='semestre',
            name='estado_semestre',
            field=models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], default='Activo', max_length=8),
        ),
    ]
