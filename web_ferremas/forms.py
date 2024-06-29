from django import forms
from .models import *

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'
        widgets = {
            "nombre": forms.TextInput(attrs={"class":"form-control", "style": "margin: 1rem"}),
            "email": forms.EmailInput(attrs={"class":"form-control", "style": "margin: 1rem"}),
            "mensaje": forms.Textarea(attrs={"class":"form-control", "style": "margin: 1rem"})
        }

        def clean_nombre(self):
            nombre = self.cleaned_data.get('nombre')
            if len(nombre) <= 2:
                raise forms.ValidationError('El nombre debe tener al menos 2 caracteres.')
            elif len(nombre)>=50:
                raise forms.ValidationError('El nombre debe tener como maximo 50 caracteres')
            return nombre

        def clean_email(self):
            email = self.cleaned_data.get('email')
            if not email.endswith('@gmail.com'):
                raise forms.ValidationError('El email debe ser del dominio @gmail.com.')
            return email

        def clean_mensaje(self):
            mensaje = self.cleaned_data.get('mensaje')
            if len(mensaje) < 10:
                raise forms.ValidationError('El mensaje debe tener al menos 10 caracteres.')
            return mensaje