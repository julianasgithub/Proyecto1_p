# Generated by Django 5.0 on 2024-01-14 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='tareas'),
        ),
    ]
