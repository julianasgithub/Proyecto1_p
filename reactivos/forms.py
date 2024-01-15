from django import forms
import decimal  #
from .models import Producto

class DescuentoForm(forms.Form):
    descuento = forms.FloatField(label='Consumido',  widget=forms.NumberInput(attrs={'step': '0.00001'}))

class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ['nombre', 'name', 'marca', 'cantidad', 'ubicacion', 'abierto', 'sedronar', 'descarte', 'categorias', 'unidades']

    def clean_cantidad(self):
        cantidad = self.cleaned_data['cantidad']
        # Realiza validaciones adicionales si es necesario
        return cantidad