from rest_framework import serializers
from .models import *

class categoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = categoria
        fields = ('id_categoria', 'nombre_categoria')
        
class usuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = usuario
        fields = ('id_usuario', 'user_name', 'user_email', 'user_password','user_type','user_suscriber')

class productoSerializer(serializers.ModelSerializer):
    class Meta:
        model = producto
        fields = ('id_producto', 'nombre_producto', 'marca_producto', 'stock_producto','categoria_producto','descripcion_producto','img_producto','id_categoria','precio_producto')

class detalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = detalle
        fields = ('id_detalle', 'id_producto', 'cantidad', 'precio')

class ventaSerializer(serializers.ModelSerializer):
    class Meta:
        model = venta 
        fields = ('id_venta', 'id_usuario', 'estado_venta', 'monto_venta','direccion_venta')
    