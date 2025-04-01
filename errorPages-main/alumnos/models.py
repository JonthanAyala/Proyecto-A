from django.db import models

# Create your models here.
class Alumnos(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    edad = models.IntegerField()
    matricula = models.CharField(max_length=10, unique=True)
    correo = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre
