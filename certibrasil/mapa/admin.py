from django.contrib import admin
from .models import cliente, endereco, certificacao

admin.site.register(cliente)
admin.site.register(endereco)
admin.site.register(certificacao)