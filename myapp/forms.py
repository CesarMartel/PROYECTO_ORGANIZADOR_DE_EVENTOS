# myapp/forms.py

from django import forms
from .models import Evento

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = '__all__' # Incluye todos los campos del modelo

        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre del Evento'}),
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'hora': forms.TimeInput(attrs={'type': 'time'}),
            'descripcion': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Detalles del evento…'}),
        }
        
        labels = {
            'nombre': 'Nombre del Evento',  
            'fecha': 'Fecha',
            'hora': 'Hora',
            'ubicacion': 'Ubicación',
            'tipo': 'Tipo de Evento',
            'descripcion': 'Descripción',
        }
