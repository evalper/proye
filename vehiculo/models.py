from django.db import models
from django.utils import timezone
from django.contrib import admin

class Conductor(models.Model):
    nombre=models.CharField(max_length=30)
    fecha_nacimiento = models.DateField()
    def __str__(self):
        return self.nombre

class Vehiculo(models.Model):
    modelo= models.CharField(max_length=60)
    placa=models.CharField(max_length=10)
    conductores=models.ManyToManyField(Conductor,through='Alquiler')

    def __str__(self):
        return self.modelo

class Alquiler(models.Model):
    conductor=models.ForeignKey(Conductor,on_delete=models.CASCADE)
    vehiculo=models.ForeignKey(Vehiculo,on_delete=models.CASCADE)
class AlquilerInLine(admin.TabularInline):
    model=Alquiler
    extra=1

class ConductorAdmin(admin.ModelAdmin):
    inlines=(AlquilerInLine,)
class VehiculoAdmin(admin.ModelAdmin):
    inlines=(AlquilerInLine,)

# Create your models here.
