# Generated by Django 5.0.3 on 2024-05-02 15:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CCSApp', '0004_alter_horario_salon_presencial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horario',
            name='salon_presencial',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CCSApp.espacio'),
        ),
    ]