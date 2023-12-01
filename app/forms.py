from django import forms
from .models import Consulta

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['fechaEntrada', 'sIntomas', 'diagnosticos', 'medicamento', 'fechaSalida', 'perro']

        widgets = {
        'fechaEntrada': forms.DateInput(attrs={'type': 'date'}),
        'fechaSalida': forms.DateInput(attrs={'type': 'date'}),
        }