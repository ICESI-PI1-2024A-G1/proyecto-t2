# Generated by Django 5.0.4 on 2024-04-14 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CCSApp', '0002_remove_horario_profesor_nrc'),
    ]

    operations = [
        migrations.AddField(
            model_name='materia',
            name='departamento',
            field=models.CharField(default='Universidad Icesi', max_length=255),
        ),
    ]
