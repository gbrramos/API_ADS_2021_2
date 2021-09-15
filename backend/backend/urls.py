from django.contrib import admin
from django.urls import path, include
from Colaboradores.views import lista 

urlpatterns = [
    path('/', admin.site.urls),
    path('colaboradores/', lista),
    
]