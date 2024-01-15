from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import DescuentoForm
from django.db.models import Q
import decimal  

from django.urls import reverse


import csv
from django.http import HttpResponse


# Create your views here.
def reactivos(request):

    productos=Producto.objects.all()
    
    return render (request, "reactivos/reactivos.html", {"productos": productos})



# en tu archivo views.py
from django.shortcuts import render, redirect
from .models import Producto
from .forms import DescuentoForm

def cargar_consumo(request, producto_id):
    producto = Producto.objects.get(id=producto_id)

    if request.method == 'POST':
        form = DescuentoForm(request.POST)
        if form.is_valid():
            descuento = form.cleaned_data['descuento']
            
            # Asegúrate de que el descuento sea del tipo Decimal
            descuento_decimal = float(descuento)

            # Realiza la operación de resta
            producto.cantidad -= descuento_decimal
            producto.save()
            
            return redirect('reactivos')  # Redirige a la vista 'reactivos'
    else:
        form = DescuentoForm()

    # Si el formulario no es válido o es una solicitud GET, renderiza la plantilla
    productos = Producto.objects.all()
    return render(request, 'reactivos/reactivos.html', {'productos': productos, 'form': form})

def buscar_productos(request):
    # Obtén la cadena de búsqueda del parámetro 'q' en la URL
    query = request.GET.get('q')

    if query:
        # Si hay una cadena de búsqueda, busca productos que coincidan con el nombre, el name o la categoría
        productos = Producto.objects.filter(
            Q(nombre__icontains=query) | Q(name__icontains=query) | Q(categorias__nombre__icontains=query)
        )
    else:
        # Si no hay cadena de búsqueda, obtén todos los productos
        productos = Producto.objects.all()

    return render(request, "reactivos/reactivos.html", {"productos": productos, "query": query})




def exportar_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="reactivos.csv"'

    writer = csv.writer(response)
    writer.writerow(['ID', 'Nombre', 'Name', 'Marca', 'Cantidad', 'Unidad', 'Categoria', 'Abierto', 'Sedronar'])

    productos = Producto.objects.all()

    for producto in productos:
        # Convierte los valores booleanos a 'si' o 'no'
        abierto = 'si' if producto.abierto else 'no'
        sedronar = 'si' if producto.sedronar else 'no'

        writer.writerow([producto.identificacion, producto.nombre, producto.name, producto.marca, producto.cantidad, producto.unidad, producto.categorias.nombre, abierto, sedronar])

    return response


import csv
from django.http import HttpResponse

def exportar_csv_sedronar(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="reactivos_sedronar.csv"'

    writer = csv.writer(response)
    writer.writerow(['ID', 'Nombre', 'Name', 'Marca', 'Cantidad', 'Unidad', 'Categoría', 'Abierto', 'Sedronar'])

    productos_sedronar = Producto.objects.filter(sedronar=True)

    for producto in productos_sedronar:
        # Convierte los valores booleanos a 'si' o 'no'
        abierto = 'si' if producto.abierto else 'no'
        sedronar = 'si' if producto.sedronar else 'no'

        writer.writerow([producto.id, producto.nombre, producto.name, producto.marca, producto.cantidad, producto.unidad, producto.categorias.nombre, abierto, sedronar])

    return response

from .forms import ProductoForm
from django import forms


def editar_reactivos(request, producto_id):
    if request.user.is_authenticated:
        producto = get_object_or_404(Producto, id=producto_id)

        if request.method == 'POST':
            form = ProductoForm(request.POST, instance=producto)
            if form.is_valid():
                form.save()
                return redirect('reactivos')  # Redirige a la vista principal después de editar
        else:
            form = ProductoForm(instance=producto)

        return render(request, 'reactivos/editar_reactivos.html', {'form': form, 'producto': producto})
    else:
        return redirect(reverse('logear')) 
    

def nuevo_reactivo(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ProductoForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('reactivos')  # Cambia 'reactivos' por el nombre de tu vista principal
        else:
            form = ProductoForm()

        return render(request, 'reactivos/nuevo_reactivo.html', {'form': form})

    else:
        return redirect(reverse('logear')) 
    