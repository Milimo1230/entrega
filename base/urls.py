from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from productos.views import inicio
from usuarios.views import somos

urlpatterns = [
    path('', inicio, name="inicio"),
    # Ruta pagina principal 
    path('somos/', somos, name="Somos"),
    path('administrador/', admin.site.urls),
    path('usuarios/',include('usuarios.urls')),
    path('facturas/',include('facturas.urls')),
    path('productos/',include('productos.urls')),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
