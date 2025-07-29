from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registro_evento, name='registro_evento'),
    path('eventos/', views.listar_eventos, name='listar_eventos'),
    path('eventos/editar/<int:id>/', views.editar_evento, name='editar_evento'),
    path('eventos/eliminar/<int:id>/', views.eliminar_evento, name='eliminar_evento'),
]

