from django import forms
from .models import Persona, Producto, Orden

# Formulario para crear/editar Persona
class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'

# Formulario para crear/editar Producto
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

# Formulario para crear Orden
class OrdenForm(forms.ModelForm):
    class Meta:
        model = Orden
        fields = '__all__'

# Formulario simple de búsqueda
class BuscarForm(forms.Form):
    termino = forms.CharField(label='Buscar persona o producto', max_length=100, required=True)
