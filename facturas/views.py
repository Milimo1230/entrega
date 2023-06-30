from django.shortcuts import render, redirect
from facturas.models import Detalle_Factura
from django.contrib.auth.decorators import login_required
from productos.carrito import Carrito
from productos.models import Producto
from facturas.forms import FacturaEnvio
from django.core.mail import EmailMessage
from django.contrib import messages
from django.urls import reverse_lazy 
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, FormView
from django.core.mail import send_mail
# Utilities
from datetime import datetime
import random
# Generar un número entero aleatorio entre 0 y 9

class FcontactoFactura(TemplateView, FormView):
    template_name = 'facturas/facturas.html'
    form_class = FacturaEnvio
    success_url = reverse_lazy('Tienda')

    def post(self, request):
        form = FacturaEnvio(request.POST)
        
        if form.is_valid():

            nombre = request.POST.get('nombre', '')
            email = request.POST.get('email', '')
            message = request.POST.get('message', '')

            send_mail(
                'Mensaje de Compra recibido',
                'Mensaje enviado por {} <{}>:\n\n{}'.format(
                    nombre, email, message),
                email,
                ['milimo1230@gmail.com'],
                fail_silently=False,
            )
            try:
                return HttpResponseRedirect(self.success_url, messages.success(self.request, f'se envio el mensaje'))
            except:
                # Ha habido un error y retorno a ERROR
                return HttpResponseRedirect(self.success_url, messages.error(self.request, f'No se envio el mensaje'))        
        return render(request, self.template_name, {'form': form })
@login_required
def contacto(request):
    formulario_contacto=FacturaEnvio() 

    if request.method=="POST":
        formulario_contacto=FacturaEnvio(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")


            email=EmailMessage("Mensaje desde App Django",
            "El usuario con nombre {} con la dirección {} escribe lo siguiente:\n\n {}".format(nombre,email,contenido),
            "",["aquí la dirección del destinatario"],reply_to=[email])
            
            try:
                email.send()
               
                return redirect("/usuarios/contacto/?valido")
            except:
                return redirect("/usuarios/contacto/?novalido")
            
    return render(request, "facturas/facturas.html", {'miFormulario':formulario_contacto})

@login_required
def factura(request):
    prostop = Producto.objects.all()
    carrito = Carrito(request)
    numero = random.randint(599999, 999999)
    now = datetime.now().strftime('%m/%d/%Y, %H:%M:%S')
    now2 = datetime.now()
    productos = Detalle_Factura.objects.all()           
    return render(request, "facturas/facturas.html", { 'now':now, 'prostop':prostop, 'numero': numero,  'carrito': carrito})
