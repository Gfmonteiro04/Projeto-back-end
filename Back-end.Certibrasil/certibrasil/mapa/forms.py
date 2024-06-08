from django import forms
from .models import Cliente, Endereco, Certificacao
from django.forms import inlineformset_factory

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'email','telefone','cnpj']

class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = ['cliente','rua', 'bairro', 'cidade', 'estado', 'zip_code', 'latitude', 'longitude', 'zip_code','cep','pais','numero']

class CertificacaoForm(forms.ModelForm):
    class Meta:
        model = Certificacao
        fields = ['cliente','nome_do_produto','quantidade','preco','data_do_pedido'] 

AddressFormSet = inlineformset_factory(Cliente, Endereco, form=EnderecoForm, extra=1)
OrderFormSet = inlineformset_factory(Cliente, Certificacao, form=CertificacaoForm, extra=1)