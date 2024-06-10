from django.contrib import admin
from django.urls import path, include
from companies.views import home_view, login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('companies.urls')),  # Inclui as URLs do aplicativo companies
    path('', home_view, name='home'),  # Ajuste para a view principal
    path('map/', include('companies.urls')),  # Para o map
    path('dashboard/', include('companies.urls')),  # Para o dashboard
    path('register/', include('companies.urls')),  # Para o register
    path('login/', login_view, name='account_login'),
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
    path('accounts/', include('allauth.urls')),  # Adiciona as URLs do Allauth
]
