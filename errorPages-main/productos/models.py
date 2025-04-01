from django.db import models

class Detalles_Productos(models.Model):
    description = models.TextField(max_length=400)
    fecha_caducidad = models.DateField()

class Provedor(models.Model):
    nombre = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

from categorias.models import Categoria

#OneToOneField ==> 1:1
#ForeignKey =====> 1:M
#ManyToManyField =>M:M  <---genera la tabla de intersecion

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.URLField()
    detalles_producto = models.OneToOneField(
        Detalles_Productos,
        null = True,
        blank=True,
        on_delete= models.CASCADE
        )
    categoria = models.ForeignKey(
        Categoria,
        null = True,
        blank=True,
        on_delete= models.CASCADE
        )
    provedor = models.ManyToManyField(
        Provedor,
        null=True,
        blank=True
        )
    

    def __str__(self):
        return self.nombre
