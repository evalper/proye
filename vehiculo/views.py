from django.shortcuts import render, get_object_or_404,redirect
from django.contrib import messages
from .forms import VehiculoForm, ConductorForm
from vehiculo.models import Vehiculo, Conductor, Alquiler
from django.contrib.auth.decorators import login_required
@login_required
def vehiculo_nuevo(request):
    if request.method=="POST":
        formulario=VehiculoForm(request.POST)
        m=request.POST.getlist('conductores')
        p=Conductor.objects.all()
        for m in m :
            ncon = Conductor.objects.get(pk=m)
        if formulario.is_valid():
           vehiculo = Vehiculo.objects.create(modelo=formulario.cleaned_data['modelo'])
           for conductor_id in request.POST.getlist('conductores'):
               vhi = Alquiler(conductor_id=conductor_id, vehiculo_id = vehiculo.id)
               vhi.save()
        return redirect('vehiculo_detalle', pk=vehiculo.pk)
    else:
        formulario = VehiculoForm()
    return render(request, 'vehiculo_editar.html', {'formulario': formulario})
@login_required
def conductor_nuevo(request):
  if request.method == "POST":
     formulario = ConductorForm(request.POST)
     if formulario.is_valid():
        conductor = Conductor.objects.create(nombre=formulario.cleaned_data['nombre'],fecha_nacimiento=formulario.cleaned_data['fecha_nacimiento'])
     return redirect('detalle_conductor',pk=conductor.id)
  else:
      formulario = ConductorForm()
  return render(request, 'conductor_nuevo.html', {'formulario': formulario})
@login_required
def editar_conductor(request, pk):
    conductor = get_object_or_404(conductor, pk=pk)
    if request.method == "POST":
        formulario = conductorForm(request.POST, instance=conductor)
        if formulario.is_valid():
            conductor = formulario.save(commit=False)
            conductor.save()
            return redirect('conductor', pk=conductor.id)
    else:
       formulario = conductorForm(instance=conductor)
    return render(request, 'conductor_nuevo.html', {'formulario': formulario})
@login_required
def editar_conductor(request, pk):
    conduc = get_object_or_404(Conductor, pk=pk)
    if request.method == "POST":
        formulario = ConductorForm(request.POST, instance=conduc)
        if formulario.is_valid():
            conduc = formulario.save(commit=False)
            conduc.save()
            return redirect('detalle_conductor', pk=conduc.id)
    else:
       formulario = ConductorForm(instance=conduc)
    return render(request, 'conductor_editar.html', {'formulario': formulario})


#..............................
def listar_vehiculos(request):
    vh=Vehiculo.objects.all()
    return render(request,'listar_vehiculos.html',{'vh':vh})

def listar_conductores(request):
    con=Conductor.objects.all()
    return render(request,'listar_conductores.html',{'con':con})

def vehiculo_detalle(request,pk):
        p=get_object_or_404(Vehiculo, pk=pk)
        datos=[]
        vt=Alquiler.objects.filter(vehiculo_id=pk)
        for vt in vt :
            nve = Conductor.objects.get(pk=vt.conductor_id)
            datos.append (nve)
        return render(request,'vehiculo_detalle.html', {'p':p,'datos':datos})

def detalle_conductor(request,pk):
    p=get_object_or_404(Conductor, pk=pk)
    return render(request,'detalle_conductor.html', {'p':p})

def eliminar_vehiculo(request, pk):
    v = get_object_or_404(Vehiculo, pk=pk)
    v.delete()
    return redirect('/')
# Create your views here.
