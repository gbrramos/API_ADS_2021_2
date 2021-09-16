from django.urls import path

from . import views

urlpatterns = [
    path('', views.lista, name='postos-trabalho-lista'),
    path('novo/', views.novo, name="postos-trabalho-novo"),
    path('editar/<int:id>', views.edit, name="postos-trabalho-editar"),
    path('delete/<int:id>', views.delete, name="postos-trabalho-delete"),
    path('view/<int:id>', views.view, name="postos-trabalho-view"),

  
]