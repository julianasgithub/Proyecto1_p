# Generated by Django 5.0 on 2024-01-11 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipamiento', '0004_rename_ubicación_post_responsable_post_ubicacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='POE',
            field=models.FileField(blank=True, null=True, upload_to='equipamiento'),
        ),
    ]