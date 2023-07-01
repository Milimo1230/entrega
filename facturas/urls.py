from django.urls import path
from facturas.views import FcontactoFactura, factura 

urlpatterns = [
    path('', FcontactoFactura.as_view(), name='enviFactura'),      
    path('', factura,name="factura"),  
]