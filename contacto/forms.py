from django import forms


class FormularioContacto(forms.Form):
    nombre = forms.CharField(label="Nombre", required=True, max_length=100)
    email = forms.CharField(label="E-mail", required=True, max_length=100)
    mensaje = forms.CharField(label="Mensaje", widget=forms.Textarea)