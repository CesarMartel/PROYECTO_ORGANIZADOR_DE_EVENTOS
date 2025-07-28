# myapp/forms.py

from django import forms
from .models import Evento

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = '__all__' # Incluye todos los campos del modelo

        # Opcional: Personalizar widgets para usar los tipos de input HTML5 y placeholders
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre del Evento'}),
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'hora': forms.TimeInput(attrs={'type': 'time'}),
            'descripcion': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Detalles del evento…'}),
        }
        
        # Opcional: Personalizar labels (si difieren de los nombres de campo del modelo)
        labels = {
            'nombre': 'Nombre del Evento',  
            'fecha': 'Fecha',
            'hora': 'Hora',
            'ubicacion': 'Ubicación',
            'tipo': 'Tipo de Evento',
            'descripcion': 'Descripción',
        }

    # Aquí podrías añadir opciones de ubicación fijas para el select, si lo deseas
    # Aunque tu HTML ya tiene las opciones hardcodeadas, Django puede generarlas
    # si defines choices en el modelo o en el formulario.
    # Por ahora, como el modelo es CharField, simplemente se enviará el valor.
    # Si quieres que la selección de distrito sea más robusta,
    # podríamos definir choices en el modelo o en el formulario.
    # Por ejemplo:
    # UBICACION_CHOICES = [
    #     ('Ancón', 'Ancón'),
    #     ('Ate', 'Ate'),
    #     # ... todas tus opciones ...
    # ]
    # ubicacion = forms.ChoiceField(choices=UBICACION_CHOICES)