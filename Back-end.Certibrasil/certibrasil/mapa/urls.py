from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    ClienteListView, ClienteDetailView, ClienteCreateView, ClienteUpdateView, ClienteDeleteView,
    EnderecoListView, EnderecoDetailView, EnderecoCreateView, EnderecoUpdateView, EnderecoDeleteView,
    CertificacaoListView, CertificacaoDetailView, CertificacaoCreateView, CertificacaoUpdateView, CertificacaoDeleteView
)

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('clientes/', ClienteListView.as_view(), name='cliente_list'),
    path('clientes/<int:pk>/', ClienteDetailView.as_view(), name='cliente_detail'),
    path('clientes/new/', ClienteCreateView.as_view(), name='cliente_create'),
    path('clientes/<int:pk>/edit/', ClienteUpdateView.as_view(), name='cliente_update'),
    path('clientes/<int:pk>/delete/', ClienteDeleteView.as_view(), name='cliente_delete'),

    path('enderecos/', EnderecoListView.as_view(), name='endereco_list'),
    path('enderecos/<int:pk>/', EnderecoDetailView.as_view(), name='endereco_detail'),
    path('enderecos/new/', EnderecoCreateView.as_view(), name='endereco_create'),
    path('enderecos/<int:pk>/edit/', EnderecoUpdateView.as_view(), name='endereco_update'),
    path('enderecos/<int:pk>/delete/', EnderecoDeleteView.as_view(), name='endereco_delete'),

    path('certificacoes/', CertificacaoListView.as_view(), name='certificacao_list'),
    path('certificacoes/<int:pk>/', CertificacaoDetailView.as_view(), name='certificacao_detail'),
    path('certificacoes/new/', CertificacaoCreateView.as_view(), name='certificacao_create'),
    path('certificacoes/<int:pk>/edit/', CertificacaoUpdateView.as_view(), name='certificacao_update'),
    path('certificacoes/<int:pk>/delete/', CertificacaoDeleteView.as_view(), name='certificacao_delete'),
]
