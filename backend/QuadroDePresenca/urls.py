from django.urls import path

from . import views

urlpatterns = [
    path('lista/', views.lista, name='quadro-presenca-lista'),
    path('novo/', views.novo, name="quadro-presenca-novo"),
    path('editar/<int:id>', views.edit, name="quadro-presenca-editar"),
    path('delete/<int:id>', views.delete, name="quadro-presenca-delete"),
    path('view/<int:id>', views.view, name="postos-trabalho-view"),
]