from django.views.generic import ListView  

from .models import certibrasil 

 

class ListListView(ListView):  

    model = certibrasil  

    template_name = "mapa/index.html" 