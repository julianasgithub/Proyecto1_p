# Generated by Django 5.0 on 2024-01-11 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materiales', '0004_rename_ubicación_material_ubicacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='materiales'),
        ),
    ]
