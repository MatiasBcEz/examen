from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(usuario)
admin.site.register(categoria)
admin.site.register(venta)
admin.site.register(detalle)
admin.site.register(producto)