from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
import requests
from .models import Producto, Categoria
from .forms import ProductoForm

def lista_productos(request):
    orden = request.GET.get('orden', 'nombre')
    productos = Producto.objects.all().order_by(orden)
    return render(request, 'lista_productos.html', {'productos': productos})

def gestionar_producto(request, id=None):
    if id:
        producto = get_object_or_404(Producto, id=id)
    else:
        producto = None
    
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm(instance=producto)
    
    return render(request, 'formulario_producto.html', {'form': form})

def detalle_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    return render(request, 'detalle_producto.html', {'producto': producto})

def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos')
    return render(request, 'detalle_producto.html', {'producto': producto})

def importar_productos_api(request):
    response = requests.get('https://fakestoreapi.com/products')
    if response.status_code == 200:
        productos_api = response.json()
        for item in productos_api:
            categoria, _ = Categoria.objects.get_or_create(nombre=item['category'])
            Producto.objects.get_or_create(
                nombre=item['title'],
                precio=item['price'],
                stock=10,
                categoria=categoria,
                descripcion=item['description']
            )
        return HttpResponse("Productos importados con éxito.")
    return HttpResponse("Error al importar productos.")