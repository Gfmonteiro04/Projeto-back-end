import logging
import csv
from django.shortcuts import render, redirect
from rest_framework import viewsets
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.core.files.storage import default_storage
from django.db.models.signals import pre_save
from django.dispatch import receiver
from geopy.geocoders import Nominatim
from django.contrib.auth.forms import UserCreationForm
from .models import Company, Certification
from .serializers import CompanySerializer, CertificationSerializer

logger = logging.getLogger(__name__)

def map_view(request):
    return render(request, 'companies/map.html')

def dashboard_view(request):
    companies = Company.objects.all()
    return render(request, 'companies/dashboard.html', {'companies': companies})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account_login')
    else:
        form = UserCreationForm()
    return render(request, 'companies/registration/register.html', {'form': form})


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['get'])
    def filter_by_certification(self, request):
        cert_name = request.query_params.get('certification', None)
        if cert_name:
            companies = Company.objects.filter(certifications__name=cert_name)
        else:
            companies = Company.objects.all()
        serializer = self.get_serializer(companies, many=True)
        return Response(serializer.data)

class CertificationViewSet(viewsets.ModelViewSet):
    queryset = Certification.objects.all()
    serializer_class = CertificationSerializer
    permission_classes = [IsAuthenticated]

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upload_csv(request):
    try:
        file = request.FILES['file']
        logger.info(f"Received file: {file.name}")
        
        file_path = default_storage.save(f'tmp/{file.name}', file)
        logger.info(f"File saved to: {file_path}")

        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                logger.info(f"Processing row: {row}")
                certifications = row['certifications'].split(';')
                cert_objects = []
                for cert in certifications:
                    obj, created = Certification.objects.get_or_create(name=cert.strip())
                    cert_objects.append(obj)
                company = Company.objects.create(
                    name=row['name'],
                    street=row['street'],
                    number=row['number'],
                    zip_code=row['zip_code'],
                    city=row['city'],
                    state=row['state']
                )
                company.certifications.set(cert_objects)
                company.save()
        return Response({"status": "success"})
    except Exception as e:
        logger.error(f"Error uploading CSV: {e}")
        return Response({"status": "error", "message": str(e)}, status=500)

@receiver(pre_save, sender=Company)
def add_lat_long(sender, instance, **kwargs):
    geolocator = Nominatim(user_agent="myGeocoder")
    location = geolocator.geocode(f"{instance.street} {instance.number}, {instance.city}, {instance.state}, {instance.zip_code}")
    if location:
        instance.latitude = location.latitude
        instance.longitude = location.longitude
