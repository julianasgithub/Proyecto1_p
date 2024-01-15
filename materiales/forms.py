from django import forms
from .models import Material

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['titulo', 'ubicacion', 'unidad', 'cantidad']

    def clean_cantidad(self):
        cantidad = self.cleaned_data['cantidad']
        # Realiza validaciones adicionales si es necesario
        return cantidad
    
