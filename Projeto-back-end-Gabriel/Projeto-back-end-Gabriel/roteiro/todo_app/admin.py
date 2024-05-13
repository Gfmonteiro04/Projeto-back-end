from django.contrib import admin

# Register your models here.
from django.contrib import admin 

from todo_app.models import ToDoItem, ToDoList, Client, Address, Certification

 

admin.site.register(ToDoItem) 

admin.site.register(ToDoList) 
admin.site.register(Client)
admin.site.register(Address)
admin.site.register(Certification)   
