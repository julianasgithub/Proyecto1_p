from django.db import models

# Create your models here.

class Tarea(models.Model):
    titulo=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=50)
    responsable=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to='tareas', null=True, blank=True)
    
    created=models.DateField(auto_now_add=True) 
    updated=models.DateField(auto_now_add=True) 

    class Meta:
        verbose_name='tarea'
        verbose_name_plural='tareas'
    def __str__(self):
        return self.titulo    