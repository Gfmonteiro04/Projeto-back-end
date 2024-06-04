from django.utils import timezone  
from django.db import models  
from django.urls import reverse
from django.contrib.auth.models import User

#models cliente
def one_week_hence():  
    return timezone.now() + timezone.timedelta(days=7)  

class cliente(models.Model):  
    title = models.CharField(max_length=100, unique=True)  
    def get_absolute_url(self):  
        return reverse("cliente", args=[self.id])  
    def _str_(self):  
        return self.title  

class endereco(models.Model):  
    title = models.CharField(max_length=100)  
    description = models.TextField(null=True, blank=True)  
    created_date = models.DateTimeField(auto_now_add=True)  
    due_date = models.DateTimeField(default=one_week_hence)  
    endereco = models.ForeignKey(cliente, on_delete=models.CASCADE)  
    def get_absolute_url(self):  
        return reverse("endereco-update", args=[str(self.lista.id), str(self.usuario.id)])  
    
    def _str_(self):  
        return f"{self.title}: due {self.due_date}"  

    class Meta:
        ordering = ["due_date"]

class certificacao(models.Model):  
    title = models.CharField(max_length=100)  
    description = models.TextField(null=True, blank=True)  
    created_date = models.DateTimeField(auto_now_add=True)  
    due_date = models.DateTimeField(default=one_week_hence)  
    certificacao = models.ForeignKey(cliente, on_delete=models.CASCADE)  
    def get_absolute_url(self):  
        return reverse("certificacao-update", args=[str(self.lista.id), str(self.usuario.id)])  
    
    def _str_(self):  
        return f"{self.title}: due {self.due_date}"  

    class Meta:
        ordering = ["due_date"]