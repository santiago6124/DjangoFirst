from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length = 20, default="Categoria")
    descripcion = models.TextField(default="Descripcion")

    def __str__(self):
        return self.nombre



class Direccion(models.Model):
    calle = models.CharField(max_length=30, default="Calle")
    numero = models.IntegerField(default=1)
    comuna = models.CharField(max_length=30, default="Comuna")
    ciudad = models.CharField(max_length=30, default="Ciudad")
    def __str__(self):
        return self.calle 


class Proveedor(models.Model):
    nombre = models.CharField(max_length=30,default="Proveedor")
    telefono = models.BigIntegerField(default=1)
    web = models.URLField(default="google.com")
    direccion = models.ManyToManyField(Direccion)

    def __str__(self):
        return self.nombre 

class Cliente(models.Model):
    nombre = models.CharField(max_length=30, default="Nombre")
    direccion = models.ManyToManyField(Direccion)

    def __str__(self):
        return self.nombre 

class Telefono(models.Model):
    telefono = models.CharField(max_length =10, default="3513897259")
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE, default=1
    )
    def __str__(self):
        return self.telefono 

class Producto(models.Model):
    nombre = models.CharField(max_length = 20, default="Nombre")
    precio = models.IntegerField(default=1)
    stock = models.IntegerField( default=1)

    Cat = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE, default=1
    )
    Prov = models.ForeignKey(
        Proveedor,
        on_delete=models.CASCADE, default=1
    )

    def __str__(self):
        return self.nombre 
        
class Venta(models.Model):
    Fecha = models.DateField(default= "2022-09-06")
    descuento = models.IntegerField( default=1)
    
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE, default=1
    )

class Detalle(models.Model):
    cantidad = models.IntegerField (default=1)
    Prod = models.ForeignKey(
        Producto,
        on_delete=models.CASCADE, default=1
    )
    Venta = models.ForeignKey(
        Venta,
        on_delete=models.CASCADE, default=1
    )
    