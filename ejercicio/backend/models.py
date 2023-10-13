from django.db import models

class Cliente(models.Model):
    dpi=models.CharField(max_length=13)
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    telefono=models.CharField(max_length=8)
    direccion=models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
  
class Proveedores(models.Model):
    nombre=models.CharField(max_length=50)
    direccion=models.CharField(max_length=50)
    telefono=models.CharField(max_length=8)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Banco(models.Model):
    nombre=models.CharField(max_length=50)
    direccion=models.CharField(max_length=50)
    telefono=models.CharField(max_length=8)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Tarjeta(models.Model):
    numero=models.CharField(max_length=16)
    codigoVerificacion=models.IntegerField()
    fechaVencimiento=models.CharField(max_length=5)
    idCliente=models.ForeignKey(Cliente, on_delete=models.CASCADE)
    idBanco=models.ForeignKey(Banco, on_delete=models.CASCADE)
    idProveedores=models.ForeignKey(Proveedores, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
   