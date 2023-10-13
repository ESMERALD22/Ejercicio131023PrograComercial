from django.shortcuts import render
from django.http.response import JsonResponse
from django.views import View
from .models import *
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from django.db.models import F


# Create your views here.
class TarjetaView(View):
    @method_decorator(csrf_exempt)  # Saltamos restriccion
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, req, id=0):
        id = int(id)
        if id > 0:
            tajetas = list(
                Tarjeta.objects.select_related("idCliente,idProveedores,idBanco")
                .filter(id=id)
                .values(
                    Id=F("id"),
                    IdCliente=F("idCliente__id"),
                    IdBanco=F("idBanco__id"),
                    IdProveedor=F("idProveedores__id"),
                    Nombre=F("idCliente__nombre"),
                    Apellido=F("idCliente__apellido"),
                    DPI=F("idCliente__dpi"),
                    Numero_Tarjeta=F("numero"),
                    Codigo_Verificación=F("codigoVerificacion"),
                    Fecha_Vencimiento=F("fechaVencimiento"),
                    Banco=F("idBanco__nombre"),
                    Proveedor=F("idProveedores__nombre"),
                )
            )
            if len(tajetas) > 0:
                tajeta = tajetas[0]
                data = {"message": "SUCCESS", "Tarjeta": tajeta}
            else:
                data = {"message": "ERROR, tarjeta not found..."}
            return JsonResponse(data)
        else:
            tajetas = list(
                Tarjeta.objects.select_related("idCliente,idProveedores,idBanco").values(
                    Id=F("id"),
                    IdCliente=F("idCliente__id"),
                    IdBanco =F("idBanco__id"),
                    IdProveedor= F("idProveedores__id"),
                    Nombre=F("idCliente__nombre"),
                    Apellido=F("idCliente__apellido"),
                    DPI=F("idCliente__dpi"),
                    Numero_Tarjeta=F("numero"),
                    Codigo_Verificación=F("codigoVerificacion"),
                    Fecha_Vencimiento=F("fechaVencimiento"),
                    Banco= F("idBanco__nombre"),
                    Proveedor= F("idProveedores__nombre"),
                )
            )
            if len(tajetas) > 0:
                data = {"message": "SUCCESS", "Tarjetas": tajetas}
            else:
                data = {"message": "ERROR, tarjetas not found..."}
            return JsonResponse(data)


class TarjetaByClienteView(View):
    @method_decorator(csrf_exempt)  # Saltamos restriccion
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, req, id=0):
        id = int(id)
        if id > 0:
            tajetas = list(
                Tarjeta.objects.select_related("idCliente,idBanco,idProveedores")
                .filter(idCliente_id=id)
                .values(
                    Id=F("id"),
                    IdCliente=F("idCliente__id"),
                    IdBanco=F("idBanco__id"),
                    IdProveedor=F("idProveedores__id"),
                    Nombre=F("idCliente__nombre"),
                    Apellido=F("idCliente__apellido"),
                    DPI=F("idCliente__dpi"),
                    Numero_Tarjeta=F("numero"),
                    Codigo_Verificación=F("codigoVerificacion"),
                    Fecha_Vencimiento=F("fechaVencimiento"),
                    Banco=F("idBanco__nombre"),
                    Proveedor=F("idProveedores__nombre"),
                )
            )
            if len(tajetas) > 0:
                data = {"message": "SUCCESS", "Tarjeta": tajetas}
            else:
                data = {"message": "ERROR, tarjeta del cliente no encontrada..."}
            return JsonResponse(data)
        else:
            data = {"message": "ERROR, tarjeta del cliente no encontrada..."}
            return JsonResponse(data)


class TarjetaByProveedoresView(View):
    @method_decorator(csrf_exempt)  # Saltamos restriccion
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, req, id=0):
        id = int(id)
        if id > 0:
            tajetas = list(Tarjeta.objects.select_related("idProveedores,idCliente,idBanco").filter(idProveedores_id=id).values(
                    Id=F("id"),
                    IdCliente=F("idCliente__id"),
                    IdBanco =F("idBanco__id"),
                    IdProveedor= F("idProveedores__id"),
                    Nombre=F("idCliente__nombre"),
                    Apellido=F("idCliente__apellido"),
                    DPI=F("idCliente__dpi"),
                    Numero_Tarjeta=F("numero"),
                    Codigo_Verificación=F("codigoVerificacion"),
                    Fecha_Vencimiento=F("fechaVencimiento"),
                    Banco= F("idBanco__nombre"),
                    Proveedor= F("idProveedores__nombre"),
                ))
            if len(tajetas) > 0:
                data = {"message": "SUCCESS", "Tarjeta": tajetas}
            else:
                data = {
                    "message": "ERROR proveedores, tarjeta del cliente no encontrada..."
                }
            return JsonResponse(data)
        else:
            data = {
                "message": "ERROR proveedores, tarjeta del cliente no encontrada..."
            }
            return JsonResponse(data)


class TarjetaByBancoView(View):
    @method_decorator(csrf_exempt)  # Saltamos restriccion
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, req, id=0):
        id = int(id)
        if id > 0:
            tajetas = list(Tarjeta.objects.select_related("idBanco,idCliente,idProveedores").filter(idBanco_id=id).values(
                    Id=F("id"),
                    IdCliente=F("idCliente__id"),
                    IdBanco =F("idBanco__id"),
                    IdProveedor= F("idProveedores__id"),
                    Nombre=F("idCliente__nombre"),
                    Apellido=F("idCliente__apellido"),
                    DPI=F("idCliente__dpi"),
                    Numero_Tarjeta=F("numero"),
                    Codigo_Verificación=F("codigoVerificacion"),
                    Fecha_Vencimiento=F("fechaVencimiento"),
                    Banco= F("idBanco__nombre"),
                    Proveedor= F("idProveedores__nombre"),
                ))
            if len(tajetas) > 0:
                data = {"message": "SUCCESS", "Tarjeta": tajetas}
            else:
                data = {"message": "ERROR banco, tarjeta del cliente no encontrada..."}
            return JsonResponse(data)
        else:
            data = {"message": "ERROR banco, tarjeta del cliente no encontrada..."}
            return JsonResponse(data)
