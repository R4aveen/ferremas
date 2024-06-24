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