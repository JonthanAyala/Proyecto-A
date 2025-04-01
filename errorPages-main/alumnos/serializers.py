from .models import Alumnos
from rest_framework import serializers

class AlumnosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumnos
        fields = '__all__'
