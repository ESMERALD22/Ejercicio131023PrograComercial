from .views import *
from .view2 import *

from django.urls import path

urlpatterns = [
    path("tarjeta/", TarjetaView.as_view(), name="tarjeta_list"),
    path("tarjeta/<int:id>",TarjetaView.as_view(),name="tarjeta_process"),
    path("tarjetaByCliente/<int:id>",TarjetaByClienteView.as_view(),name="tarjetaC_process"),
    path("tarjetaByBanco/<int:id>",TarjetaByBancoView.as_view(),name="tarjetaB_process"),
    path("tarjetaByProveedores/<int:id>",TarjetaByProveedoresView.as_view(),name="tarjetaP_process"),
    path("tarjetaRow/", TarjetaViewRow.as_view(), name="tarjeta_list"),
    path("tarjetaRow/<int:id>",TarjetaViewRow.as_view(),name="tarjeta_process"),
    path("tarjetaBancoRow/<int:id>",TarjetaBancoViewRow.as_view(),name="tarjeta_process"),
    path("tarjetaProveedorRow/<int:id>",TarjetaProveedorViewRow.as_view(),name="tarjeta_process"),
    path("tarjetaClienteRow/<int:id>",TarjetaClienteViewRow.as_view(),name="tarjeta_process"),
   
]