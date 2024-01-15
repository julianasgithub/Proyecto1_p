from django.urls import path
from . import views
from .views import cargar_archivo, nuevo_equipamiento, editar_equipamiento, buscar_equipamiento

urlpatterns = [
    path('', views.equipamiento, name='equipamiento'),
    #path('categoria/<int:categoria_id>/', views.categoria, name="categoria"),
    path('cargar_archivo/<int:equipamiento_id>/', cargar_archivo, name='cargar_archivo'),
    path('nuevo_equipamiento/', nuevo_equipamiento, name='nuevo_equipamiento'),
    path('editar_equipamiento/<int:equipamiento_id>/', editar_equipamiento, name='editar_equipamiento'),
    path('buscar_equipamiento/', buscar_equipamiento, name='buscar_equipamiento'),
]
