# Generated by Django 5.0.4 on 2024-04-28 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CCSApp', '0003_remove_programacionacademica_materia_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='programacionacademica',
            name='modalidad',
        ),
        migrations.AddField(
            model_name='programacionacademica',
            name='horario',
            field=models.ManyToManyField(to='CCSApp.horario'),
        ),
    ]
