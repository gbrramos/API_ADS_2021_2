from Colaboradores import views
from PostosDeTrabalho import views
from Clientes import views
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('colaboradores/', include('Colaboradores.urls')),
    path('postosTrabalho/', include('PostosDeTrabalho.urls')),
    path('clientes/', include('Clientes.urls')),

]