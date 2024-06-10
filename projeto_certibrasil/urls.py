from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from companies.views import home_view, map_view, dashboard_view, register, login_view, CompanyViewSet, CertificationViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'certifications', CertificationViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', home_view, name='home'),  # Ajuste para a view principal
    path('map/', map_view, name='map_view'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('register/', register, name='register'),
    path('login/', login_view, name='account_login'),
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
    path('accounts/', include('allauth.urls')),  # Adiciona as URLs do Allauth
    path('api/', include('companies.urls')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),    
]
