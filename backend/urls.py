"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.shortcuts import redirect
from django.urls import path
from eventos import views

urlpatterns = [
    path('', lambda request: redirect('registro_evento')),  # ← Redirige al registro automáticamente
    path('registro/', views.registro_evento, name='registro_evento'),
    path('eventos/editar/<int:id>/', views.editar_evento, name='editar_evento'),
    path('eventos/eliminar/<int:id>/', views.eliminar_evento, name='eliminar_evento'),
]



