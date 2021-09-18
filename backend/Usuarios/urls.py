from django.urls import path

from . import views

urlpatterns = [
    path('lista', views.lista, name='usuarios-lista'),
    path('novo/', views.novo, name="usuarios-novo"),
    path('editar/<int:id>', views.editar, name="usuarios-editar"),
    path('delete/<int:id>', views.delete, name="usuarios-delete"),
    path('view/<int:id>', views.view, name="usuarios-view"),
]