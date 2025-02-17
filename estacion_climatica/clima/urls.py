from django.urls import path
from .views import *

urlpatterns = [
    path('', graficos, name="graficos"),
    path('obtener-meses/', obtener_meses, name='obtener_meses'),
]
