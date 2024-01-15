from django.urls import path
from . import views
from .views import cargar_consumo, buscar_productos, exportar_csv, exportar_csv_sedronar, editar_reactivos, nuevo_reactivo


urlpatterns = [
    
    
    path('reactivos/', views.reactivos, name='reactivos'),
 
    path('cargar_consumo/<int:producto_id>/', cargar_consumo, name='cargar_consumo'),
    path('buscar_productos/', buscar_productos, name='buscar_productos'),
     path('exportar_csv/', exportar_csv, name='exportar_csv'),
     path('exportar_csv_sedronar/', exportar_csv_sedronar, name='exportar_csv_sedronar'),
     path('editar_reactivos/<int:producto_id>/', editar_reactivos, name='editar_reactivos'),
     path('nuevo_reactivo/', nuevo_reactivo, name='nuevo_reactivo'),
]

