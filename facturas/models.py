from django.db import models


class Detalle_Factura(models.Model):
    cod_fac = models.IntegerField(primary_key=True, verbose_name='Código')
    detalle_producto = models.CharField(max_length=42, blank=True, null=True)
    cantidad = models.IntegerField(blank=True)
    precio_unitario = models.IntegerField(blank=True)
    precio_total = models.IntegerField(blank=True)
    cliente = models.CharField (max_length=50, blank=True)
    direccion_envio = models.CharField (max_length=150, blank=True,verbose_name="Dirección de Envío")
    telefono = models.CharField (max_length=50)  
    fecha_compra = models.DateTimeField(blank=True)
    def __str__(self):
        return'{}'.format(self.cod_fac)
    
    class Meta:
        verbose_name_plural="Detalles Facturas"
        verbose_name="Detalle Factura"

class Metodos_pago(models.Model):
    metodo = models.CharField(max_length=30, blank=True, null=True)