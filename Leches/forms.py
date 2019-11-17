from django import forms
from .models import Leche

class LecheForm(forms.ModelForm):
    class Meta:
        model = Leche
        fields = ['Nombre', 'FechaVencimiento', 'Cantidad', 'LoteProducto']