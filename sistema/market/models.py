from django.db import models

# Create your models here.
class Producto(models.Model):
    id= models.AutoField(primary_key=True)
    titulo= models.CharField(max_length= 200)
    autor= models.CharField(max_length = 100)
    materia = models.CharField(max_length=200, default="General")
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits = 10, decimal_places=2)
    stock = models.IntegerField()