from django.contrib import admin
from .models import Producto
from .models import Direccion
from .models import Categoria
from .models import Proveedor
from .models import Cliente
from .models import Telefono
from .models import Detalle
from .models import Venta




# Register your models here.
admin.site.register(Producto)
admin.site.register(Direccion)
admin.site.register(Categoria)
admin.site.register(Proveedor)
admin.site.register(Cliente)
admin.site.register(Telefono)
admin.site.register(Detalle)
admin.site.register(Venta)

