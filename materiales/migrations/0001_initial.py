# Generated by Django 5.0 on 2023-12-31 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='materiales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('contenido', models.CharField(max_length=50)),
                ('unidad', models.CharField(max_length=50)),
                ('cantidad', models.FloatField()),
                ('imagen', models.ImageField(upload_to='')),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'material',
                'verbose_name_plural': 'materiales',
            },
        ),
    ]