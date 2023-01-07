"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ejemplo.views import (monstrar_celulares, BuscarCelular, AltaCelular, ActualizarCelular, CelularDetalle, CelularList, CelularCrear, CelularBorrar, CelularActualizar)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('celulares/', monstrar_celulares),
    path('celulares/buscar', BuscarCelular.as_view()),
    path('celulares/alta', AltaCelular.as_view()),
    path('celulares/actualizar/<int:pk>', ActualizarCelular.as_view()),
    path('panel-celulares/<int:pk>/detalle', CelularDetalle.as_view()),
    path('panel-celulares/', CelularList.as_view()),
    path('panel-celulares/crear', CelularCrear.as_view()),
    path('panel-celulares/<int:pk>/borrar', CelularBorrar.as_view()),
    path('panel-celulares/<int:pk>/actualizar', CelularActualizar.as_view()),
]
