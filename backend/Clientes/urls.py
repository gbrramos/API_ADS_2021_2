from django.urls import path

from . import views

urlpatterns = [
    path('lista', views.lista, name='clientes-lista'),
    path('novo/', views.novo, name="clientes-novo"),
    path('editar/<int:id>', views.editar, name="clientes-editar"),
    path('delete/<int:id>', views.delete, name="clientes-delete"),
    path('view/<int:id>', views.view, name="clientes-view"),
]