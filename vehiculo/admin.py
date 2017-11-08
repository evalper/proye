from django.contrib import admin
from vehiculo.models import Conductor,ConductorAdmin,Vehiculo,VehiculoAdmin

admin.site.register(Conductor,ConductorAdmin)
admin.site.register(Vehiculo,VehiculoAdmin)

# Register your models here.
