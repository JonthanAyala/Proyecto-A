from django import forms
from .models import Alumnos

class AlumnoForm(forms.ModelForm):
    id = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'readonly': 'readonly',
                'placeholder': 'ID del alumno este campo no se puede modificar'
            }
        ),
        required=False
    )
    class Meta:
        model = Alumnos
        fields = ['id','nombre',
                    'apellidos',
                      'edad', 'matricula', 'correo']
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el nombre del alumno',
                    'pattern': '[A-Za-z ]+',
                    'title': 'Solo se permiten letras y espacios'
                }
            ),
            'apellidos': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese los apellidos del alumno',
                    'pattern': '[A-Za-z ]+',
                    'title': 'Solo se permiten letras y espacios'
                }
            ),
            'edad': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese la edad del alumno',
                    'min': 0,
                    'max': 100,
                    'title': 'Ingresa un valor entre 0 y 100'
                }
            ),
            'matricula': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese la matricula del alumno',
                    'pattern': '^\d{5}TN\d{3}$',
                    'title': 'Solo se permiten letras y numeros'
                }
            ),
            'correo': forms.EmailInput(
                attrs={
                    'type': 'email',
                    'class': 'form-control',
                    'placeholder': 'Ingrese el correo del alumno',
                    'pattern': '^\[a-zA-Z0-9._%+-]+@utez\.edu\.mx$',
                    'title': 'Ingresa un correo valido'
                }
            )
        }
        labels = {
            'nombre': 'Nombre del Alumno',
            'apellidos': 'Apellidos del Alumno',
            'edad': 'Edad del Alumno',
            'matricula': 'Matricula del Alumno',
            'correo': 'Correo del Alumno'
        }
        error_messages = {
            'edad':{
                'required': 'La edad no puede estar vacia',
                'invalid': 'Ingresa un valor valido'
            }
        }
        
