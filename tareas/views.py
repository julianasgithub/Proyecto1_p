
from django.shortcuts import render, redirect, get_object_or_404
from tareas.models import Tarea
from django import forms
from django.db.models import Q
from .models import Tarea
from tareas.forms import TareaForm
from django.urls import reverse


# Create your views here.
def tareas(request):

    tareas=Tarea.objects.all()
    
    return render (request, "tareas/tareas.html", {"tareas": tareas})

# Create your views here.

def nueva_tarea(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = TareaForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('tareas')  # Redirige a la vista principal después de crear
        else:
            form = TareaForm()

        return render(request, 'tareas/nueva_tarea.html', {'form': form})
    else:
        return redirect(reverse('logear')) 
    
def editar_tarea(request, tarea_id):
    if request.user.is_authenticated:
        tarea = get_object_or_404(Tarea, id=tarea_id)

        if request.method == 'POST':
            form = TareaForm(request.POST, request.FILES, instance=tarea)
            if form.is_valid():
                form.save()
                return redirect('tareas')  # Redirige a la vista principal después de editar
        else:
            form = TareaForm(instance=tarea)

        return render(request, 'tareas/editar_tarea.html', {'form': form, 'producto': tarea})
    else:
        return redirect(reverse('logear')) 