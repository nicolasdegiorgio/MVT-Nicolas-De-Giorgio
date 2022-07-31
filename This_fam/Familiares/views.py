from django.shortcuts import render
from django.http import HttpResponse
from Familiares.models import listado_familiares
from django.template import Template, Context, loader


# Create your views here.

#Vista principal de index    
def string_familia(request):
    #Traigo todos los objetos del DB
    familia = listado_familiares.objects.all()
    #Hago el listado para empezar a generar el contexto
    listado= []
    for count, items in enumerate(familia):
        
        listado.append(f'El familiar n° {count+1} se llama {items.nombre} {items.apellido}, y su contacto es {items.email}')
         
    #Genero contexto para renderizar el template
    datos = {'Familiares': listado}
    
    #Retorno el renderizado de template y apunto a /index.html
    return render(request, 'Familiares/index.html', datos)