from django.db import models

# Create your models here.
class SliderIndex(models.Model):
    numero = models.CharField(max_length=15,primary_key=True)
    foto = models.ImageField(upload_to='index',null=True)

    def __str__(self):
        return self.numero

class SliderGaleria(models.Model):
    numero = models.CharField(max_length=15,primary_key=True)
    foto = models.ImageField(upload_to='galeria',null=True)

    def __str__(self):
        return self.numero

class MisionVision(models.Model):
    numero = models.CharField(max_length=115,primary_key=True)
    mision = models.TextField()
    vision = models.TextField()

    def __str__(self):
        return self.numero

class Insumos(models.Model):
    nombre = models.CharField(max_length=120,primary_key=True)
    precio = models.IntegerField()
    stock = models.IntegerField()
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre