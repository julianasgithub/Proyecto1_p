# Generated by Django 5.0 on 2024-01-06 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reactivos', '0002_producto_created_producto_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
