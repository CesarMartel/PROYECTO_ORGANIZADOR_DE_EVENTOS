# myapp/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Evento
from .forms import EventoForm

# Vista para listar eventos y manejar el registro de nuevos eventos
def lista_eventos(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_eventos') # Redirige a la misma página después de guardar
    else:
        form = EventoForm() # Formulario vacío para GET request

    eventos = Evento.objects.all() # Obtiene todos los eventos
    return render(request, 'index.html', {'form': form, 'eventos': eventos})

# Vista para editar un evento existente
def editar_evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk) # Obtiene el evento 
    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento) # Pasa la instancia para actualizar
        if form.is_valid():
            form.save()
            return redirect('lista_eventos')
    else:
        form = EventoForm(instance=evento) # Rellena el formulario con los datos del evento

    eventos = Evento.objects.all()
    return render(request, 'index.html', {'form': form, 'eventos': eventos, 'edit_mode': True, 'evento_id': pk})

# Vista para eliminar un evento
def eliminar_evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    if request.method == 'POST': 
        evento.delete()
        return redirect('lista_eventos')

    return redirect('lista_eventos')

def inicio(request):
    return render(request, 'inicio.html')
