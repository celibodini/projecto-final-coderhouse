from django.db import models

# Create your models here.

class Celulares(models.Model):
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=200)
    precio = models.IntegerField()
def __str__(self):
      return f"{self.nombre}, {self.marca}, {self.id}"