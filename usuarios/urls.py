from django.urls import path, include
from .import views
from usuarios.views import VRegistro, contacto, email, ayuda

urlpatterns = [
    path('',views.usuarios,name="usuarios"), 
    path('registro',VRegistro.as_view(), name="registro"),          
    path('accounts/', include('django.contrib.auth.urls')),    
    #mail
    path('contacto', email.as_view(),name='correo'),     
    path('ayuda/', ayuda, name='ayuda'),     
]