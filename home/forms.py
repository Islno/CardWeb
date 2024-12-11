from django import forms
from .models import Categoria

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['id', 'nome', 'ordem']
        widgets = {
            'id': forms.NumberInput(attrs={'class': 'form-control'}),
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'ordem': forms.NumberInput(attrs={'class': 'form-control'}),
        }