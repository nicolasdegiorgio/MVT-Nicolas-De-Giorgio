from django.shortcuts import render
from django.http import HttpResponse
from Familiares.models import listado_familiares
# Create your views here.


def lista_familiares(request):
    familia = listado_familiares.objects.all()
    
    lista_familiares_nombres=[]
    
    for items in familia:
        lista_familiares_nombres.append(items.nombre)
        
        

    return HttpResponse(lista_familiares_nombres)



def string_familia(request):
    
    familia = listado_familiares.objects.all()
    
    listado= []
    for count, items in enumerate(familia):
        
        listado.append(f'El familiar n° {count+1} se llama {items.nombre} {items.apellido}, y su contacto es {items.email}')
        a = print(listado[items])
        
    return HttpResponse (a)
   