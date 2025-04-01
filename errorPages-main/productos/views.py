from .models import Producto
from .serializers import ProductosSerializer
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from .forms import ProductoForm
from django.shortcuts import render

class ProductoViewset(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductosSerializer
    renderer_classes = [JSONRenderer]
    # http_method_names = ['GET', 'POST']

def agregar_productos(request):
    form = ProductoForm()
    return render(request, 'agregar.html', {'form': form})
    