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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from ejemplo.views import (monstrar_celulares, BuscarCelular, AltaCelular, ActualizarCelular, CelularDetalle, CelularList, CelularCrear, CelularBorrar, CelularActualizar)
from ejemplo_celulares.views import (index, PostDetalle, PostListar, 
                               PostCrear, PostBorrar, PostActualizar,
                               UserSignUp, UserLogin, UserLogout, 
                               AvatarActualizar, UserActualizar, MensajeCrear, MensajeListar, MensajeDetalle )
from django.contrib.admin.views.decorators import staff_member_required


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
    path('success_updated_message/',TemplateView.as_view(template_name="ejemplo/success_updated_message.html")),
    path('ejemplo-celulares/', index, name="ejemplo-celulares-index"),
    path('ejemplo-celulares/<int:pk>/detalle/', PostDetalle.as_view(), name="ejemplo-celulares-detalle"),
    path('ejemplo-celulares/listar/', PostListar.as_view(), name="ejemplo-celulares-listar"),
    path('ejemplo-celulares/crear/', staff_member_required(PostCrear.as_view()), name="ejemplo-celulares-crear"),
    path('ejemplo-celulares/<int:pk>/borrar/', staff_member_required(PostBorrar.as_view()), name="ejemplo-celulares-borrar"),
    path('ejemplo-celulares/<int:pk>/actualizar/', staff_member_required(PostActualizar.as_view()), name="ejemplo-celulares-actualizar"),
    path('ejemplo-celulares/signup/', UserSignUp.as_view(), name ="ejemplo-celulares-signup"),
    path('ejemplo-celulares/login/', UserLogin.as_view(), name= "ejemplo-celulares-login"),
    path('ejemplo-celulares/logout/', UserLogout.as_view(), name="ejemplo-celulares-logout"),
    path('ejemplo-celulares/avatars/<int:pk>/actualizar/', AvatarActualizar.as_view(), name="ejemplo-celulares-avatars-actualizar"),
    path('ejemplo-celulares/users/<int:pk>/actualizar/', UserActualizar.as_view(), name="ejemplo-celulares-users-actualizar"),
    path('ejemplo-celulares/mensajes/crear/', MensajeCrear.as_view(), name="ejemplo-celulares-mensajes-crear"),
    path('ejemplo-celulares/mensajes/<int:pk>/detalle/', MensajeDetalle.as_view(), name="ejemplo-celulares-mensajes-detalle"),
    path('ejemplo-celulares/mensajes/listar/', MensajeListar.as_view(), name="ejemplo-celulares-mensajes-listar"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)