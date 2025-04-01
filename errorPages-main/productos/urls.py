from django.urls import path, include
from .views import *
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'api',ProductoViewset)

urlpatterns = [
    path('',include(router.urls)),
    path('agregar/', agregar_productos , name='agregar_p')
]