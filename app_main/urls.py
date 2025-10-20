from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('persona/', views.nueva_persona, name='persona'),
    path('producto/', views.nuevo_producto, name='producto'),
    path('orden/', views.nueva_orden, name='orden'),
    path('buscar/', views.buscar, name='buscar'),
]
