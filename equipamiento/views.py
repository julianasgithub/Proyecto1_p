from django.shortcuts import render, redirect, get_object_or_404
from equipamiento.models import Equipamiento
from django import forms
from django.db.models import Q
from django.urls import reverse
# Create your views here.



from django.shortcuts import render, redirect
from .forms import EquipamientoForm
from .models import Equipamiento


def equipamiento(request):
    equipamientos=Equipamiento.objects.all()
    return render (request, "equipamiento/equipamiento.html", {"equipamientos":equipamientos})

def cargar_archivo(request, equipamiento_id):
    equipamiento = get_object_or_404(Equipamiento, id=equipamiento_id)

    if request.method == 'POST':
        form = EquipamientoForm(request.POST, request.FILES, instance=equipamiento)
        if form.is_valid():
            equipamiento.manual = form.cleaned_data['manual']
            equipamiento.save()
            return render (request, "equipamiento/equipamiento.html", {"equipamiento":equipamiento})
    else:
        form = EquipamientoForm(instance=equipamiento)

    return render(request, 'equipamiento/cargar_archivo.html', {'form': form, 'equipamiento': equipamiento})

def nuevo_equipamiento(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = EquipamientoForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('equipamiento')  # Cambia 'reactivos' por el nombre de tu vista principal
        else:
            form = EquipamientoForm()

        return render(request, 'equipamiento/nuevo_equipamiento.html', {'form': form})

    else:
        return redirect(reverse('logear')) 
    
    
def editar_equipamiento(request, equipamiento_id):
    equipamiento = get_object_or_404(Equipamiento, id=equipamiento_id)
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = EquipamientoForm(request.POST, request.FILES, instance=equipamiento)
            if form.is_valid():
                form.save()
                return redirect('equipamiento')  # Redirige a la vista principal después de editar
        else:
            form = EquipamientoForm(instance=equipamiento)

        return render(request, 'equipamiento/editar_equipamiento.html', {'form': form, 'equipamiento': equipamiento})
    else:
        return redirect(reverse('logear')) 
def buscar_equipamiento(request):
    # Obtén la cadena de búsqueda del parámetro 'q' en la URL
    query = request.GET.get('q')

    if query:
        # Si hay una cadena de búsqueda, busca productos que coincidan con el nombre, el name o la categoría
        equipamientos = Equipamiento.objects.filter(
             Q(titulo__icontains=query) | Q(contenido__icontains=query) | Q(responsable__icontains=query) | Q(categorias__icontains=query)
        )
        
    else:
        # Si no hay cadena de búsqueda, obtén todos los productos
        equipamientos = Equipamiento.objects.all()

    return render(request, "equipamiento/equipamiento.html", {"equipamientos": equipamientos, "query": query})

