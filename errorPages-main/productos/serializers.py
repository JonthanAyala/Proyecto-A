from .models import Producto
from rest_framework import serializers

class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'
