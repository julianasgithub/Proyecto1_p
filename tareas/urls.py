from django.urls import path
from . import views
from .views import nueva_tarea, editar_tarea
urlpatterns = [
  
    path('', views.tareas, name='tareas'),
     path('nueva_tarea/', nueva_tarea, name='nueva_tarea'),
     path('editar_tarea/<int:tarea_id>/', editar_tarea, name='editar_tarea'),
    
]

