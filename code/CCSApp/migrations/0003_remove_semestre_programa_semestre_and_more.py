# Generated by Django 5.0.4 on 2024-04-29 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CCSApp', '0002_alter_programacionacademica_id_programacionacademica'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='semestre',
            name='programa_semestre',
        ),
        migrations.AddField(
            model_name='semestre',
            name='programa_semestre',
            field=models.ManyToManyField(default='', to='CCSApp.programa_de_posgrado'),
        ),
    ]
