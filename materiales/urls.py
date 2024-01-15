from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import  buscar_materiales
from .views import editar_material, nuevo_material, exportar_csv_mat
urlpatterns = [
   
    path('', views.materiales, name='material'),
    path('buscar_materiales/', buscar_materiales, name='buscar_materiales'),
    path('editar_material/<int:material_id>/', editar_material, name='editar_material'),
     path('nuevo_material/', nuevo_material, name='nuevo_material'),
     path('exportar_csv_mat/', exportar_csv_mat, name='exportar_csv_mat'),
     
]

