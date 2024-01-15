from django import forms
from .models import Equipamiento

class EquipamientoForm(forms.ModelForm):
    class Meta:
        model = Equipamiento
        fields = ['titulo', 'contenido', 'ubicacion', 'manual', 'POE', 'responsable', 'imagen', 'categorias']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['manual'].widget.attrs.update({'accept': 'application/pdf'})  # Limita a archivos PDF