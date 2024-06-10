from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet, CertificationViewSet, map_view, dashboard_view, register, login_view, upload_csv

router = DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'certifications', CertificationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('map/', map_view, name='map_view'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('register/', register, name='register'),
    path('login/', login_view, name='account_login'),
    path('upload-csv/', upload_csv, name='upload_csv'),
]
