# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_eventos, name='lista_eventos'), # Tu CRUD principal
    path('inicio/', views.inicio, name='inicio'), # Nueva URL para la página de inicio
    path('editar/<int:pk>/', views.editar_evento, name='editar_evento'),
    path('eliminar/<int:pk>/', views.eliminar_evento, name='eliminar_evento'),
]