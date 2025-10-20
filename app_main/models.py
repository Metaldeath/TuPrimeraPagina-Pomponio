from django.db import models

# Modelo Persona: datos básicos de una persona
class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    correo = models.EmailField()

    def __str__(self):
        return self.nombre

# Modelo Producto: nombre, precio y stock
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre

# Modelo Orden: relaciona Persona y Producto (muchas ordenes)
class Orden(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.persona} - {self.producto} ({self.fecha.strftime('%Y-%m-%d %H:%M')})"
