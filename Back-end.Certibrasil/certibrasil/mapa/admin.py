from django.contrib import admin

from .models import Cliente, Endereco, Certificacao 

admin.site.register(Cliente)  
admin.site.register(Endereco) 
admin.site.register(Certificacao)
