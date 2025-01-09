from django import forms
from .models import Categoria, Cliente
from datetime import date


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome', 'ordem']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}),
            'ordem': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ordem'}),
        }
        labels = {
            'nome': 'Informe o nome da categoria: ',
            'ordem': 'Informe a ordem: ',
        }

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'cpf', 'datanasc']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}),
            'cpf': forms.TextInput(attrs={'class': 'cpf form-control', 'placeholder': 'C.P.F'}),
            'datanasc': forms.DateInput(attrs={'class': 'data form-control', 'placeholder': 'Data de Nascimento'}, format='%d/%m/%Y'),
        }
        labels = {
            'nome': 'Informe o nome do cliente: ',
            'cpf': 'Informe o CPF: ',
            'datanasc': 'Informe a data de nascimento: ',
        }

    def clean_nome(self):
        nome = self.cleaned_data.get('nome')
        if len(nome) < 3:
            raise forms.ValidationError("O nome deve ter pelo menos 3 caracteres.")
        return nome
    def clean_datanasc(self):
        datanasc = self.cleaned_data.get('datanasc')
        if datanasc > date.today():
            raise forms.ValidationError('A data de nascimento não pode ser maior que a data atual.')
        return datanasc
    