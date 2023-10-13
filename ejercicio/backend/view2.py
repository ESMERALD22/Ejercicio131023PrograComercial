from django.shortcuts import render
from django.http.response import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
from .models import *


class TarjetaViewRow(View):
    @method_decorator(csrf_exempt)  # Saltamos la restricción CSRF
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, req, id=0):
        id = int(id)
        with connection.cursor() as cursor:
            if id > 0:
                cursor.execute(
                    """ SELECT backend_banco.id as "idBanco", backend_banco.nombre as "Banco", backend_proveedores.id as "idProveedores", backend_proveedores.nombre as "Proveedores", backend_cliente.dpi, backend_cliente.nombre , backend_cliente.apellido, backend_tarjeta.numero, backend_tarjeta."codigoVerificacion", backend_tarjeta."fechaVencimiento"  FROM backend_banco  INNER JOIN backend_tarjeta ON backend_banco.id = backend_tarjeta."idBanco_id"  INNER JOIN backend_proveedores ON backend_tarjeta."idProveedores_id" = backend_proveedores.id INNER JOIN backend_cliente on backend_tarjeta."idCliente_id" = backend_cliente.id WHERE backend_tarjeta.id = %s  """,
                    [id],
                )
                row = cursor.fetchone()
                if row:
                    data = {
                        "message": "SUCCESS",
                        "Tarjeta": dict(
                            zip([col[0] for col in cursor.description], row)
                        ),
                    }
                else:
                    data = {"message": "ERROR, tarjeta not found..."}
            else:
                cursor.execute("""SELECT backend_banco.id as "idBanco", backend_banco.nombre as "Banco", backend_proveedores.id as "idProveedores", backend_proveedores.nombre as "Proveedores", backend_cliente.dpi, backend_cliente.nombre , backend_cliente.apellido, backend_tarjeta.numero, backend_tarjeta."codigoVerificacion", backend_tarjeta."fechaVencimiento"  FROM backend_banco  INNER JOIN backend_tarjeta ON backend_banco.id = backend_tarjeta."idBanco_id"  INNER JOIN backend_proveedores ON backend_tarjeta."idProveedores_id" = backend_proveedores.id INNER JOIN backend_cliente on backend_tarjeta."idCliente_id" = backend_cliente.id  """)
                rows = cursor.fetchall()
                if rows:
                    data = {
                        "message": "SUCCESS",
                        "Tarjetas": [
                            dict(zip([col[0] for col in cursor.description], row))
                            for row in rows
                        ],
                    }
                else:
                    data = {"message": "ERROR, tarjetas not found..."}
        return JsonResponse(data)


class TarjetaBancoViewRow(View):
    @method_decorator(csrf_exempt)  # Saltamos la restricción CSRF
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, req, id=0):
        id = int(id)
        with connection.cursor() as cursor:
            if id > 0:
                cursor.execute(
                    """ SELECT backend_banco.id as "idBanco", backend_banco.nombre as "Banco", backend_proveedores.id as "idProveedores", backend_proveedores.nombre as "Proveedores", backend_cliente.dpi, backend_cliente.nombre , backend_cliente.apellido, backend_tarjeta.numero, backend_tarjeta."codigoVerificacion", backend_tarjeta."fechaVencimiento"  FROM backend_banco  INNER JOIN backend_tarjeta ON backend_banco.id = backend_tarjeta."idBanco_id"  INNER JOIN backend_proveedores ON backend_tarjeta."idProveedores_id" = backend_proveedores.id INNER JOIN backend_cliente on backend_tarjeta."idCliente_id" = backend_cliente.id WHERE backend_banco.id = %s """,
                    [id],
                )
                rows = cursor.fetchall()
                if rows:
                    data = {
                        "message": "SUCCESS",
                        "Tarjetas": [
                            dict(zip([col[0] for col in cursor.description], row))
                            for row in rows
                        ],
                    }
                else:
                    data = {"message": "ERROR, tarjeta de bancos no encontradas..."}
            else:
                data = {"message": "ERROR, tarjetas de bancos no encontradas..."}
        return JsonResponse(data)


class TarjetaProveedorViewRow(View):
    @method_decorator(csrf_exempt)  # Saltamos la restricción CSRF
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, req, id=0):
        id = int(id)
        with connection.cursor() as cursor:
            if id > 0:
                cursor.execute(
                    """ SELECT backend_banco.id as "idBanco", backend_banco.nombre as "Banco", backend_proveedores.id as "idProveedores", backend_proveedores.nombre as "Proveedores", backend_cliente.dpi, backend_cliente.nombre , backend_cliente.apellido, backend_tarjeta.numero, backend_tarjeta."codigoVerificacion", backend_tarjeta."fechaVencimiento"  FROM backend_banco  INNER JOIN backend_tarjeta ON backend_banco.id = backend_tarjeta."idBanco_id"  INNER JOIN backend_proveedores ON backend_tarjeta."idProveedores_id" = backend_proveedores.id INNER JOIN backend_cliente on backend_tarjeta."idCliente_id" = backend_cliente.id WHERE backend_proveedores.id = %s """,
                    [id],
                )
                rows = cursor.fetchall()
                if rows:
                    data = {
                        "message": "SUCCESS",
                        "Tarjetas": [
                            dict(zip([col[0] for col in cursor.description], row))
                            for row in rows
                        ],
                    }
                else:
                    data = {"message": "ERROR, tarjeta de bancos no encontradas..."}
            else:
                data = {"message": "ERROR, tarjetas de bancos no encontradas..."}
        return JsonResponse(data)

class TarjetaClienteViewRow(View):
    @method_decorator(csrf_exempt)  # Saltamos la restricción CSRF
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, req, id=0):
        id = int(id)
        with connection.cursor() as cursor:
            if id > 0:
                cursor.execute(
                    """ SELECT backend_banco.id as "idBanco", backend_banco.nombre as "Banco", backend_proveedores.id as "idProveedores", backend_proveedores.nombre as "Proveedores", backend_cliente.dpi, backend_cliente.nombre , backend_cliente.apellido, backend_tarjeta.numero, backend_tarjeta."codigoVerificacion", backend_tarjeta."fechaVencimiento"  FROM backend_banco  INNER JOIN backend_tarjeta ON backend_banco.id = backend_tarjeta."idBanco_id"  INNER JOIN backend_proveedores ON backend_tarjeta."idProveedores_id" = backend_proveedores.id INNER JOIN backend_cliente on backend_tarjeta."idCliente_id" = backend_cliente.id WHERE backend_cliente.id = %s """,
                    [id],
                )
                rows = cursor.fetchall()
                if rows:
                    data = {
                        "message": "SUCCESS",
                        "Tarjetas": [
                            dict(zip([col[0] for col in cursor.description], row))
                            for row in rows
                        ],
                    }
                else:
                    data = {"message": "ERROR, tarjeta de bancos no encontradas..."}
            else:
                data = {"message": "ERROR, tarjetas de bancos no encontradas..."}
        return JsonResponse(data)

