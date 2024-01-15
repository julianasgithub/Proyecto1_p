from django.db import models

# Create your models here.

class CategoriaProd(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="categoriaProd"
        verbose_name_plural="categoriasProd"

    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    identificacion=models.CharField(max_length=10)
    categorias=models.ForeignKey(CategoriaProd, on_delete=models.CASCADE)
    ubicacion = models.CharField(max_length=50, default="Armario Amarillo N°2")
    marca=models.CharField(max_length=50)
    CAS=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to="reactivos", null=True, blank=True)
    cantidad=models.FloatField()
    unidad=models.CharField(max_length=10)
    unidades=models.IntegerField(default=1)
    abierto=models.BooleanField(default=True)
    sedronar=models.BooleanField(default=True)
    descarte = models.CharField(max_length=500, default='Reactivos...')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)



    class Meta:
        verbose_name="Producto"
        verbose_name_plural="Productos"
    def __str__(self):
        return self.nombre