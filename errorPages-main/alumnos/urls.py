from django.urls import path, include
from .views import *
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'api',ALumnosViewset)

urlpatterns = [
    path('',include(router.urls)),
    path('index/', index, name='index'),
]