# Generated by Django 5.0 on 2024-01-07 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('materiales', '0003_rename_contenido_material_ubicación'),
    ]

    operations = [
        migrations.RenameField(
            model_name='material',
            old_name='ubicación',
            new_name='ubicacion',
        ),
    ]
