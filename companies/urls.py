from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet, CertificationViewSet, map_view, upload_csv, register, dashboard_view

router = DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'certifications', CertificationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('upload-csv/', upload_csv, name='upload_csv'),
    path('map/', map_view, name='map_view'),
    path('register/', register, name='register'),
    path('dashboard/', dashboard_view, name='dashboard'),
]
