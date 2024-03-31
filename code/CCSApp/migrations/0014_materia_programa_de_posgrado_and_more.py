# Generated by Django 5.0.3 on 2024-03-31 23:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CCSApp', '0013_merge_20240330_2013'),
    ]

    operations = [
        migrations.AddField(
            model_name='materia',
            name='programa_de_posgrado',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='CCSApp.programa_de_posgrado'),
        ),
        migrations.AlterField(
            model_name='programa_de_posgrado',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]