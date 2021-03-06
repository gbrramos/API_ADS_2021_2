from django.contrib.auth import authenticate
from Colaboradores import views
from PostosDeTrabalho import views
from Clientes import views
from Usuarios import views
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('colaboradores/', include('Colaboradores.urls')),
    path('postosTrabalho/', include('PostosDeTrabalho.urls')),
    path('clientes/', include('Clientes.urls')),
    path('usuarios/', include('Usuarios.urls')),
    path('contratos/', include('Contratos.urls')),
    path('quadroPresenca/', include('QuadroPresenca.urls')),
    path('alocacoes/', include('Alocacoes.urls')),
    path('dashboard/', include('Dashboard.urls')),
    path('', lambda request: redirect('login/')),
    path('', include('Usuarios.urls')),
]