# Generated by Django 5.0 on 2024-01-02 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('materiales', '0002_material_delete_materiales'),
    ]

    operations = [
        migrations.RenameField(
            model_name='material',
            old_name='contenido',
            new_name='ubicación',
        ),
    ]
