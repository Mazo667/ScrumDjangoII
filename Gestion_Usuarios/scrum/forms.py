from django import forms
from .models import Tarea

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'fecha_de_finalizacion', 'estado', 'responsable', 'sprint_asignado', 'dependencias', 'bloqueadores']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-tarea', 'placeholder': 'Título de la tarea'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-tarea', 'placeholder': 'Descripción de la tarea'}),
            'fecha_de_finalizacion': forms.DateInput(attrs={'class': 'form-tarea', 'type': 'date'}),
            'bloqueadores': forms.Textarea(attrs={'class': 'form-tarea', 'placeholder': 'Bloquadores de la tarea'}),
        }