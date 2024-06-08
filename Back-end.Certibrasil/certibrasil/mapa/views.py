from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Cliente, Endereco, Certificacao

class ClienteListView(ListView):
    model = Cliente
    template_name = 'cliente_list.html'

class ClienteDetailView(DetailView):
    model = Cliente
    template_name = 'cliente_detail.html'

class ClienteCreateView(LoginRequiredMixin, CreateView):
    model = Cliente
    template_name = 'cliente_form.html'
    fields = ['nome', 'email', 'telefone', 'cnpj']

class ClienteUpdateView(LoginRequiredMixin, UpdateView):
    model = Cliente
    template_name = 'cliente_form.html'
    fields = ['nome', 'email', 'telefone', 'cnpj']

class ClienteDeleteView(LoginRequiredMixin, DeleteView):
    model = Cliente
    template_name = 'cliente_confirm_delete.html'
    success_url = reverse_lazy('cliente_list')

class EnderecoListView(ListView):
    model = Endereco
    template_name = 'endereco_list.html'

class EnderecoDetailView(DetailView):
    model = Endereco
    template_name = 'endereco_detail.html'

class EnderecoCreateView(LoginRequiredMixin, CreateView):
    model = Endereco
    template_name = 'endereco_form.html'
    fields = ['cliente', 'rua', 'bairro', 'cidade', 'estado', 'zip_code', 'latitude', 'longitude', 'numero', 'cep', 'pais']

class EnderecoUpdateView(LoginRequiredMixin, UpdateView):
    model = Endereco
    template_name = 'endereco_form.html'
    fields = ['cliente', 'rua', 'bairro', 'cidade', 'estado', 'zip_code', 'latitude', 'longitude', 'numero', 'cep', 'pais']

class EnderecoDeleteView(LoginRequiredMixin, DeleteView):
    model = Endereco
    template_name = 'endereco_confirm_delete.html'
    success_url = reverse_lazy('endereco_list')

class CertificacaoListView(ListView):
    model = Certificacao
    template_name = 'certificacao_list.html'

class CertificacaoDetailView(DetailView):
    model = Certificacao
    template_name = 'certificacao_detail.html'

class CertificacaoCreateView(LoginRequiredMixin, CreateView):
    model = Certificacao
    template_name = 'certificacao_form.html'
    fields = ['cliente', 'nome_do_produto', 'quantidade', 'preco']

class CertificacaoUpdateView(LoginRequiredMixin, UpdateView):
    model = Certificacao
    template_name = 'certificacao_form.html'
    fields = ['cliente', 'nome_do_produto', 'quantidade', 'preco']

class CertificacaoDeleteView(LoginRequiredMixin, DeleteView):
    model = Certificacao
    template_name = 'certificacao_confirm_delete.html'
    success_url = reverse_lazy('certificacao_list')
