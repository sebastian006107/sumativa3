from django.db import models

# Create your models here.

class Juego(models.Model):
  nombre = models.CharField(max_length=100)
  descripcion = models.TextField()
  precio = models.DecimalField(max_digits=10, decimal_places=2)
  
  def __str__(self):
    return self.nombre