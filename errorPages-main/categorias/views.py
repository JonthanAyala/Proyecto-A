import json
from django.shortcuts import get_object_or_404, render, redirect
from django.http import JsonResponse
from .models import Categoria
from .forms import CategoriaForm

def lista_categoria(request):
    categorias = Categoria.objects.all()
    data = [
        {
        'id': c.id,
        'nombre': c.nombre,
        'imagen': c.imagen
        }
        for c in categorias
    ]
    return JsonResponse(data, safe=False)

def card_categorias(request):
    return render(request, 'cards_categorias.html')

def agregar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_c')
    else:
        form = CategoriaForm()
    return render(request, 'registrar.html', {'form': form})

def guardar_categoria(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            categoria = Categoria.objects.create(
                nombre = data['nombre'],
                imagen = data['imagen'],
            )
            return JsonResponse({'mensaje': 'Registro Exitoso', 'id' : categoria.id}, status=201)
        except Exception as e:
            return JsonResponse({'error' : str(e)}, status = 400)
    return JsonResponse({'error': 'Metodo no soportado'},status = 405)
