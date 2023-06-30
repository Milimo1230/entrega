from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class FacturaEnvio(forms.Form):
    nombre = forms.CharField(label='Nombre Completo', required=True, min_length=5, max_length=25, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Introduzca sus datos'}))
    email = forms.EmailField(label='Correo Electrónico', required=True, max_length=100, widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Introduzca su email'}))
    message = forms.CharField(label='Mensaje', required=True, widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Escriba aquí su mensaje...','rows':5}))