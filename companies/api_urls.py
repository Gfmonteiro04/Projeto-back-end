from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet, CertificationViewSet, upload_csv

router = DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'certifications', CertificationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('upload-csv/', upload_csv, name='upload_csv'),
]
