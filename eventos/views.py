from django.shortcuts import render, redirect, get_object_or_404
from .models import Evento
from .forms import EventoForm

def registro_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('registro_evento')
    else:
        form = EventoForm()
    eventos = Evento.objects.all()
    return render(request, 'eventos/registro.html', {
        'form': form,
        'eventos': eventos
        })


def editar_evento(request, id):
    evento = get_object_or_404(Evento, pk=id)
    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('registro_evento')
    else:
        form = EventoForm(instance=evento)
    return render(request, 'eventos/registro.html', {'form': form, 'eventos': Evento.objects.all()})


def eliminar_evento(request, id):
    evento = get_object_or_404(Evento, pk=id)
    evento.delete()
    return redirect('registro_evento')

def listar_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'eventos/listar_eventos.html', {'eventos': eventos})

