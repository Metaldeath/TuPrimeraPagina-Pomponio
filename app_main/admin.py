from django.contrib import admin
from .models import Persona, Producto, Orden

# Registramos los modelos para poder administrarlos desde /admin/
admin.site.register(Persona)
admin.site.register(Producto)
admin.site.register(Orden)
