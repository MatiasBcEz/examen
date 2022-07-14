from django.db import models

# Create your models here.
class categoria (models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre_categoria = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre_categoria

class usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=50)
    user_email = models.EmailField()
    user_password = models.CharField(max_length=30)
    user_type = models.CharField(max_length=20)
    user_suscriber = models.CharField(max_length=3)

    def __str__(self):
        return self.user_name

class producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre_producto = models.CharField (max_length=50)
    marca_producto = models.CharField (max_length=20)
    stock_producto = models.IntegerField()
    categoria_producto = models.CharField(max_length=30)
    descripcion_producto = models.CharField(max_length=100)
    img_producto = models.ImageField()
    id_categoria = models.ForeignKey(categoria, on_delete = models.CASCADE)
    precio_producto = models.IntegerField()

    def __str__(self):
        mensaje = (f"{self.nombre_producto }, {self.marca_producto}")
        return mensaje

class detalle(models.Model):
    id_detalle = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey(producto, on_delete = models.CASCADE)
    cantidad = models.IntegerField()
    precio = models.IntegerField()

    def __str__(self):      
        return self.id_detalle

class venta(models.Model):
    id_venta = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
    estado_venta = models.CharField(max_length = 20)
    monto_venta = models.IntegerField()
    direccion_venta = models.CharField(max_length=50)

    def __str__(self):
        return self.id_venta