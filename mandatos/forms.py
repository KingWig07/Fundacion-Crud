from django import forms
from .models import MandatoAporte 

class MandatoAporteForm(forms.ModelForm):
    class Meta:
        model = MandatoAporte
        fields = ['nombre_aportador', 'rut_aportador', 'monto', 'numero_tarjeta']
        widgets = {
            'nombre_aportador': forms.TextInput(attrs={'class': 'text-field', 'placeholder': 'Ingresar Nombre', 'required': True}),
            'rut_aportador': forms.TextInput(attrs={'class': 'text-field', 'placeholder': 'Ingresar RUT', 'required': True}),
            'monto': forms.NumberInput(attrs={'class': 'text-field', 'placeholder': 'Ingresar Monto', 'required': True}),
            'numero_tarjeta': forms.TextInput(attrs={'class': 'text-field', 'placeholder': 'Ingresar Número de Tarjeta', 'required': True}),
        }

