# Generated by Django 5.0.4 on 2024-04-28 21:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CCSApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materia',
            name='departamento',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='CCSApp.departamento'),
        ),
    ]