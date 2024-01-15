from django.db import models

# Create your models here.

class Material(models.Model):
    titulo=models.CharField(max_length=50)
    ubicacion=models.CharField(max_length=50)
    unidad=models.CharField(max_length=50)
    cantidad=models.FloatField()
    imagen=models.ImageField(upload_to='materiales', null=True, blank=True)
    created=models.DateField(auto_now_add=True) 
    updated=models.DateField(auto_now_add=True) 

    class Meta:
        verbose_name='material'
        verbose_name_plural='materiales'
    def __str__(self):
        return self.titulo    