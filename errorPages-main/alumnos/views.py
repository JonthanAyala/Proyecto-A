from .models import Alumnos
from .serializers import AlumnosSerializer
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from django.shortcuts import render
from .forms import AlumnoForm

class ALumnosViewset(viewsets.ModelViewSet):
    queryset = Alumnos.objects.all()
    serializer_class = AlumnosSerializer
    renderer_classes = [JSONRenderer]

def index(request):
    form = AlumnoForm()
    return render(request, 'Ayala_Jonathan.html', {'form': form})
