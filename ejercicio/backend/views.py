from django.shortcuts import render
from django.http.response import JsonResponse
from django.views import View
from .models import *
from django.utils.decorators import method_decorator 
from django.views.decorators.csrf import csrf_exempt 
import json

# Create your views here.
class TarjetaView(View):
    @method_decorator(csrf_exempt) #Saltamos restriccion
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,req,id=0):
        id=int(id)
        if(id>0):
            tajetas=list(Tarjeta.objects.filter(id=id).values())
            if len(tajetas)>0:
                tajeta=tajetas[0]
                data={'message':"SUCCESS", 'Tarjeta':tajeta}
            else:
                data={'message':"ERROR, tarjeta not found..."}
            return JsonResponse(data)
        else:
            tajetas=list(Tarjeta.objects.values())
            if len(tajetas)>0:
                data={'message':"SUCCESS", 'Tarjetas':tajetas}
            else:
                data={'message':"ERROR, tarjetas not found..."}
            return JsonResponse(data)
    
    
class TarjetaByClienteView(View):
    @method_decorator(csrf_exempt) #Saltamos restriccion
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,req,id=0):
        id=int(id)
        if(id>0):
            tajetas=list(Tarjeta.objects.filter(idCliente_id=id).values())
            if len(tajetas)>0:
                tajeta=tajetas[0]
                data={'message':"SUCCESS", 'Tarjeta':tajeta}
            else:
                data={'message':"ERROR, tarjeta del cliente no encontrada..."}
            return JsonResponse(data)
        else:
            data={'message':"ERROR, tarjeta del cliente no encontrada..."}
            return JsonResponse(data)
    