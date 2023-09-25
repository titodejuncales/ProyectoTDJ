from django.db import models

# Create your models here.
class CamNacional(models.Model):
    nombre = models.CharField(max_length=60)
    club = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)  
    year = models.IntegerField()
    talle = models.CharField(max_length=10)
    colores = models.CharField(max_length=20)
        
    def __str__(self):
        return f"Camiseta del club {self.club} del año {self.year} marca {self.marca}" 
    
class CamSeleccion(models.Model):
    nombre = models.CharField(max_length=60)
    pais = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)  
    year = models.IntegerField()
    talle = models.CharField(max_length=10)
    colores = models.CharField(max_length=20)
   
    def __str__(self):
        return f"Camiseta del pais {self.pais} del año {self.year} marca {self.marca}" 
    
    
class CamInternacional(models.Model):
    nombre = models.CharField(max_length=60)
    club = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)  
    year = models.IntegerField()
    talle = models.CharField(max_length=10)
    colores = models.CharField(max_length=20)
      
    def __str__(self):
        return f"Camiseta del club {self.club} del año {self.year} marca {self.marca}" 
    
    