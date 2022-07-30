from django.db import models

# Create your models here.
class listado_familiares(models.Model):
    
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    documento=models.IntegerField()
    email = models.EmailField() 