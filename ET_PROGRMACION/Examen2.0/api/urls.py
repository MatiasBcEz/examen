from django.urls import URLPattern, path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', home, name="home"),

    path('login-admin', admin, name="admin"),

    path('donacion', donacion, name="donacion"),
    path('contacto', contacto, name="contacto"),
    path('quienessomos', quienessomos, name="quienessomos"),
    path('sucursales', sucursales, name="sucursales"),
    path('terminos', terminos, name="terminos"),

    path('alimentos', alimentos, name="alimentos"),

    path('exoticos', exoticos, name="exoticos"),
    path('gatos', gatos, name="gatos"),
    path('perros', perros, name="perros"),
    
    path('agregar_producto', agregar_producto, name="agregar_producto"),
    path('registrar_producto/', registrar_producto),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
