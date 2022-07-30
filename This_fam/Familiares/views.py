from django.shortcuts import render
from django.http import HttpResponse
from Familiares.models import listado_familiares
from django.template import Template, Context, loader


# Create your views here.


def lista_familiares(request):
    familia = listado_familiares.objects.all()
    
    lista_familiares_nombres=[]
    
    for items in familia:
        lista_familiares_nombres.append(items.nombre)
        
        

    return HttpResponse(lista_familiares_nombres)



# def string_familia(request):
    
#     familia = listado_familiares.objects.all()
    
#     listado= []
#     for count, items in enumerate(familia):
        
#         listado.append(f'El familiar n° {count+1} se llama {items.nombre} {items.apellido}, y su contacto es {items.email}')
#         return listado
#     #Hacemos un render para tomar la plantilla
    
#     datos = {'Familiares': listado}
    
#     #Creamos la plantilla
    
#     plantilla=loader.get_template('Familia/index.html')
    
    
#     documento=plantilla.render(datos)
    
#     return HttpResponse(documento)
        
        
#     #return HttpResponse (listado)
   
   
def string_familia(request):
    
    familia = listado_familiares.objects.all()
    
    listado= []
    for count, items in enumerate(familia):
        
        listado.append(f'El familiar n° {count+1} se llama {items.nombre} {items.apellido}, y su contacto es {items.email}')
        #return listado  
    
    datos_contexto = {'Familiares': listado}
    
    archivo = open(r'G:\Mi unidad\Curso Python\Clase 18 - Django II\Desafio entregable\This_fam\Familiares\templates\index.html', 'r')
    contenidohtml=archivo.read()
    archivo.close()
    
    #crear la plantilla
    plantilla=Template(contenidohtml)
    
    #crear contexto
    contexto=Context(datos_contexto)
    
    #preparar documento para renderizar
    documento_a_renderizar=plantilla.render(contexto)
    
    #devolver la respuesta al usuario
    return HttpResponse(documento_a_renderizar)