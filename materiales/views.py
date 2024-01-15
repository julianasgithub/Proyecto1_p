from django.shortcuts import render, redirect, get_object_or_404
from materiales.models import Material
from django import forms
from django.db.models import Q
from django.urls import reverse

import csv
from django.http import HttpResponse


# Create your views here.

def materiales(request):
    materiales=Material.objects.all()
    return render (request,"materiales/material.html", {'materiales': materiales})

def buscar_materiales(request):
    # Obtén la cadena de búsqueda del parámetro 'q' en la URL
    query = request.GET.get('q')

    if query:
        # Si hay una cadena de búsqueda, busca productos que coincidan con el nombre, el name o la categoría
        materiales = Material.objects.filter(
            Q(titulo__icontains=query)
        )
    else:
        # Si no hay cadena de búsqueda, obtén todos los productos
        productos = Material.objects.all()

    return render(request, "materiales/material.html", {"materiales": materiales, "query": query})

from materiales.forms import MaterialForm

def editar_material(request, material_id):
    material = get_object_or_404(Material, id=material_id)
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = MaterialForm(request.POST, request.FILES, instance=material)
            if form.is_valid():
                form.save()
                return redirect('material')  # Redirige a la vista principal después de editar
        else:
            form = MaterialForm(instance=material)

        return render(request, 'materiales/editar_material.html', {'form': form, 'material': material})
    else:
        return redirect(reverse('logear')) 
    
def nuevo_material(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = MaterialForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('material')  # Redirige a la vista principal después de crear
        else:
            form = MaterialForm()

        return render(request, 'materiales/nuevo_material.html', {'form': form})
    else:
        return redirect(reverse('logear')) 
    
import csv
from django.http import HttpResponse

def exportar_csv_mat(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="materiales.csv"'

    writer = csv.writer(response)
    writer.writerow(['titulo', 'ubicacion', 'cantidad'])

    materiales= Material.objects.all()

    for material in materiales:
       

        writer.writerow([material.titulo, material.ubicacion,f'{material.unidad}: {material.cantidad} unidades'])

    return response

