from django.urls import path
from .views import *

urlpatterns = [
    path('api/get/', card_categorias, name='lista_c'),
    path('registrar/', agregar_categoria, name='agregar_c'),
    path('json/', lista_categoria, name='json'),
    path('api/guardar/', guardar_categoria, name='guardar_c')
]