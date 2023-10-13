from .views import *
from django.urls import path

urlpatterns = [
    path("tarjeta/", TarjetaView.as_view(), name="tarjeta_list"),
    path("tarjeta/<int:id>",TarjetaView.as_view(),name="tarjeta_process"),
    path("tarjetaByCliente/<int:id>",TarjetaByClienteView.as_view(),name="tarjetaC_process"),
]
