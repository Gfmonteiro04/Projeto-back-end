from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from geopy.geocoders import Nominatim

class Certification(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    number = models.CharField(max_length=10)
    zip_code = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    certifications = models.ManyToManyField(Certification)

    def __str__(self):
        return self.name

@receiver(pre_save, sender=Company)
def add_lat_long(sender, instance, **kwargs):
    geolocator = Nominatim(user_agent="myGeocoder")
    location = geolocator.geocode(f"{instance.street} {instance.number}, {instance.city}, {instance.state}, {instance.zip_code}")
    if location:
        instance.latitude = location.latitude
        instance.longitude = location.longitude
