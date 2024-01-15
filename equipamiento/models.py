from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Equipamiento(models.Model):
    titulo=models.CharField(max_length=50)
    ubicacion=models.CharField(max_length=50)
    contenido=models.CharField(max_length=500)
    manual=models.FileField(upload_to='equipamiento', null=True, blank=True) 
    POE=models.FileField(upload_to='equipamiento', null=True, blank=True)
    imagen=models.ImageField(upload_to='equipamiento', null=True, blank=True)
    responsable=models.CharField(max_length=50)
    created=models.DateField(auto_now_add=True) 
    updated=models.DateField(auto_now_add=True)
    cat_electroq='electroquimico'
    cat_general='general'
    OPCIONES_CATEGORIA = [
        (cat_electroq, 'Equipamiento Electroquímico'),
        (cat_general, 'Equipamiento General'),
    ]

    categorias = models.CharField(max_length=50,choices=OPCIONES_CATEGORIA,null=True,blank=True
    )
    
    
    class Meta:
        verbose_name='equipamiento'
        verbose_name_plural='equipamientos'
    def __str__(self):
        return self.titulo