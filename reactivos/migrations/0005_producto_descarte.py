# Generated by Django 5.0 on 2024-01-08 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reactivos', '0004_producto_sedronar_alter_producto_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='descarte',
            field=models.FileField(blank=True, null=True, upload_to='reactivos'),
        ),
    ]