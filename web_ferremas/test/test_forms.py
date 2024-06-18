from django.test import TestCase
from web_ferremas.models import *
from web_ferremas.forms import *
from web_ferremas.urls import *


## prueba para formulario

# class TestForm(TestCase):

#     def test_tipoempleado_form_valid_data(self):
#         form_data = {'tipo_empleado': 'Administrador'}
#         form = TipoEmpleadoForm(data=form_data)
#         self.assertTrue(form.is_valid())

#     def test_tipoempleado_form_invalid(self):
#         form_data = {'tipo_empleado': 'g'*41}
#         form = TipoEmpleadoForm(data=form_data)
#         self.assertFalse(form.is_valid())
#         ## Nos asegurando de que el error esta en la descripcion
#         self.assertEqual(len(form.errors))