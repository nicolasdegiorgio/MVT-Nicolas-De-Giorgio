from django.db import models

# Create your models here.

#Creamos la clase para el DB
class listado_familiares(models.Model):
    
    
    #Agrego campos al DB
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    documento=models.IntegerField()
    email = models.EmailField() 