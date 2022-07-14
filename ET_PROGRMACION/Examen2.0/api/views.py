from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .serializers import *


# Create your views here.

def home (request):
    return render(request,'home.html')

def admin (request):
    productosListados = producto.objects.all()
    return render(request,'user/admin.html', {"productos": productosListados})

def alimentos (request):
    productosListados = producto.objects.all()
    return render(request,'tienda/alimentos.html', {"productos": productosListados})

def donacion (request):
    return render(request,'donacion.html')

def contacto (request):
    return render(request,'informacion/contacto.html')

def quienessomos (request):
    return render(request,'informacion/quienessomos.html')

def sucursales (request):
    return render(request,'informacion/sucursales.html')

def terminos (request):
    return render(request,'informacion/terminos.html')

def exoticos (request):
    return render(request,'mascotas/exoticos.html')

def gatos (request):
    return render(request,'mascotas/gatos.html')

def perros (request):
    return render(request,'mascotas/perros.html')

def agregar_producto (request):
    return render(request,'user/producto/agregar_producto.html')


@csrf_exempt
@api_view(['POST'])
def registrar_producto(request):
    product = producto.objects.create(
            nombre_producto = request.POST['id_nombre_producto'],
            marca_producto = request.POST['id_marca_producto'],
            stock_producto = request.POST['id_stock_producto'],
            categoria_producto = request.POST['id_categoria_producto'],
            descripcion_producto = request.POST['id_descripcion_producto'],
            img_producto = request.POST['id_img_producto'],
            id_categoria = request.POST['id_id_categoria'],
            precio_producto = request.POST['id_precio_producto']
        )
    product.save()
    return Response([{"mensaje": "Se Registro Correctamente"}])

@csrf_exempt
@api_view(['PUT'])
def editar_producto(request, p_id):
    try:
        product = producto.objects.get(id=p_id)
    
        product.nombre_producto = request.POST['id_nombre_producto'],
        product.marca_producto = request.POST['id_marca_producto'],
        product.stock_producto = request.POST['id_stock_producto'],
        product.categoria_producto = request.POST['id_categoria_producto'],
        product.descripcion_producto = request.POST['id_descripcion_producto'],
        product.img_producto = request.POST['id_img_producto'],
        product.id_categoria = request.POST['id_id_categoria'],
        product.precio_producto = request.POST['id_precio_producto']
        
        product.save()
        
        return Response([{"mensaje": "Se Modifico Correctamente"}])
    
    except producto.DoesNotExist:
        return Response(producto.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['DELETE'])
def eliminar_producto(request, p_id):
    try:
        product = producto.objects.get(id=p_id)
        
        product.delete()
        return Response([{"mensaje": "Se Elimino Correctamente"}])
        
    except producto.DoesNotExist:
        return Response(producto.errors, status=status.HTTP_400_BAD_REQUEST)