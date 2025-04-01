from django.http import HttpResponse
from django.shortcuts import render
from .utils import google_search
from django.http import JsonResponse
from django.shortcuts import render
from .models import ErrorLog

def index(request):
    return HttpResponse("<h1>Hola Mundo<h1>")

def error_404_view(request):
    return render(request, '404.html', status=404)

def error_500_view(request):
    return render(request, '500.html', status=500)

def error(request, exeption):
    return 7/0

def onepage(request):
    return render(request, 'onepage.html', status=200)

def prueba(request):
    nombre = request.GET.get('nombre','')
    edad = request.GET.get('edad','')
    
    persona = {
        'nombres': nombre,
        'edad': edad,
        'descripcion': nombre +'-'+edad
    }
    persona2 = {
        'nombres': 'Isai',
        'edad': '22',
        'descripcion': nombre +'-'+edad
    }
    persona3 = {
        'nombres': 'Adrian',
        'edad': '21',
        'descripcion': nombre +'-'+edad
    }

    if (persona['nombres'] == 'Ayala'):
        persona['descripcion'] = 'Ayala es wuapo'

    conjunto = [persona,persona2, persona3]
    print(persona['nombres'])
    
    return render(
        request,
        'prueba.html',
        {'objeto': persona, 'saludo': 'bienvenidos', 'personas': conjunto}
    )

def search_view(request):
    query = request.GET.get("q", "")
    results = []
    if query:
        data = google_search(query)
        results = data.get("items", [])

    return render(request, "search.html", {"results": results, "query": query})

def error_logs(request):
    return render(request, 'error_logs.html')

def get_error_logs(request):
    errors = ErrorLog.objects.values('id', 'codigo', 'mensaje', 'fecha')
    return JsonResponse({'data': list(errors)})