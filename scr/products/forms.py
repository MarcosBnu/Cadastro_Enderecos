from dataclasses import field, fields
from django import forms
from .models import Pessoa

class PessoaForm(forms.ModelForm):
    descricao= forms.CharField(max_length=150, required=False)
    complemento= forms.CharField(max_length=150, required=False)
    numero= forms.IntegerField()
    class Meta:
        model=Pessoa
        fields = ['ende', 'numero', 'complemento', 'bairro', 'cidade', 'uf' ,'descricao']

        

            