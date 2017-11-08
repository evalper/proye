from django import forms
from .models import Vehiculo, Conductor

class VehiculoForm(forms.ModelForm):
#todos los campos de Pelicula
    class Meta:
        model = Vehiculo
        fields = ('modelo', 'placa', 'conductores')
    def __init__ (self, *args, **kwargs):
        super(VehiculoForm, self).__init__(*args, **kwargs)
        self.fields["conductores"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["conductores"].help_text = "Ingrese los Actores que participaron en la película"
        self.fields["conductores"].queryset = Conductor.objects.all()

class ConductorForm(forms.ModelForm):

        class Meta:
            model = Conductor
            fields = ('nombre', 'fecha_nacimiento')
