from rest_framework import serializers
from .models import Company, Certification

class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certification
        fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):
    certifications = CertificationSerializer(many=True)

    class Meta:
        model = Company
        fields = '__all__'
