from django.conf.urls import url
from . import views

urlpatterns=[

    url(r'^vehiculo_nuevo/$',views.vehiculo_nuevo,name='vehiculo_nuevo'),
    url(r'^conductor_nuevo/$',views.conductor_nuevo,name='conductor_nuevo'),
    url(r'^$', views.listar_vehiculos),
    url(r'^listar_conductores/$', views.listar_conductores,name='listar_conductores'),
    url(r'^vehiculo_detalle/(?P<pk>[0-9]+)/$', views.vehiculo_detalle, name='vehiculo_detalle'),
    url(r'^detalle_conductor/(?P<pk>[0-9]+)/$', views.detalle_conductor, name='detalle_conductor'),
    url(r'^conductor/(?P<pk>[0-9]+)/edit/$', views.editar_conductor, name='editar_conductor'),
    url(r'^borrar_vehiculo/(?P<pk>[0-9]+)/$', views.eliminar_vehiculo, name='borrar_vehiculo'),

            ]
