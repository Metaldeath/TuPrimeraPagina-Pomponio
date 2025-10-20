# app_main/views.py
"""
Vistas de la aplicación `app_main`.
Contiene:
 - index: página principal
 - nueva_persona: formulario para crear Persona
 - nuevo_producto: formulario para crear Producto
 - nueva_orden: formulario para crear Orden
 - buscar: búsqueda en Persona y Producto (devuelve lista de dicts {'obj','tipo'})
 
Comentarios y nombres en español para facilitar mantenimiento.
"""
from django.shortcuts import render, redirect
from django.db.utils import OperationalError
from .models import Persona, Producto, Orden
from .forms import PersonaForm, ProductoForm, OrdenForm, BuscarForm


def index(request):
    """Página de inicio simple."""
    return render(request, 'index.html')


def nueva_persona(request):
    """
    Crear una nueva Persona.
    Si el POST es válido guarda y redirige al inicio.
    """
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = PersonaForm()
    return render(request, 'form_persona.html', {'form': form})


def nuevo_producto(request):
    """
    Crear un nuevo Producto.
    Si el POST es válido guarda y redirige al inicio.
    """
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = ProductoForm()
    return render(request, 'form_producto.html', {'form': form})


def nueva_orden(request):
    """
    Crear una nueva Orden.
    Si la base de datos no tiene las tablas (OperationalError) se captura y
    se muestra un mensaje amigable en la plantilla.
    """
    mensaje_error = None
    if request.method == 'POST':
        form = OrdenForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('inicio')
            except OperationalError:
                mensaje_error = "Error en la base de datos: estructura inexistente. Ejecutá las migraciones."
    else:
        form = OrdenForm()
    return render(request, 'form_orden.html', {'form': form, 'mensaje_error': mensaje_error})


def buscar(request):
    """
    Busca en Persona.nombre y Producto.nombre (case-insensitive).
    Devuelve en el contexto 'resultados' una lista homogénea de dicts:
      [{'obj': instancia, 'tipo': 'Persona'|'Producto'|'Orden'}, ...]
    Esto evita accesos a atributos con nombres que empiecen por underscore desde las plantillas.
    Si ocurre OperationalError (tabla inexistente), devuelve lista vacía.
    """
    resultados = []
    if request.method == 'POST':
        form = BuscarForm(request.POST)
        if form.is_valid():
            termino = form.cleaned_data['termino']
            try:
                # Buscar personas y productos por nombre (icontains = case-insensitive contains)
                personas = list(Persona.objects.filter(nombre__icontains=termino))
                productos = list(Producto.objects.filter(nombre__icontains=termino))
                # Buscar órdenes relacionadas (por nombre de producto o persona)
                ordenes = list(
                    Orden.objects.filter(producto__nombre__icontains=termino) |
                    Orden.objects.filter(persona__nombre__icontains=termino)
                )
                # Normalizar resultados en dicts con tipo calculado en Python
                resultados = (
                    [{'obj': p, 'tipo': type(p).__name__} for p in personas] +
                    [{'obj': pr, 'tipo': type(pr).__name__} for pr in productos] +
                    [{'obj': o, 'tipo': type(o).__name__} for o in ordenes]
                )
            except OperationalError:
                # Si la tabla(s) no existe(n), retornamos lista vacía para no romper la plantilla
                resultados = []
    else:
        form = BuscarForm()
    return render(request, 'buscar.html', {'form': form, 'resultados': resultados})
