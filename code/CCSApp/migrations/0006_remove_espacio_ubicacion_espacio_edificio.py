# Generated by Django 5.0.3 on 2024-04-07 19:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CCSApp', '0005_edificio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='espacio',
            name='ubicacion',
        ),
        migrations.AddField(
            model_name='espacio',
            name='edificio',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='CCSApp.edificio'),
        ),
    ]
