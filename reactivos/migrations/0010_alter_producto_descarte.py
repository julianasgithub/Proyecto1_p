# Generated by Django 5.0 on 2024-01-14 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reactivos', '0009_alter_producto_descarte'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='descarte',
            field=models.CharField(max_length=500),
        ),
    ]
