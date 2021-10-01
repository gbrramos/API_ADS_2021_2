from django.urls import path

from . import views

urlpatterns = [
    path('lista', views.lista, name='alocacoes-lista'),
    path('novo/', views.novo, name="alocacoes-novo"),
    path('editar/<int:id>', views.edit, name="alocacoes-editar"),
    path('delete/<int:id>', views.delete, name="alocacoes-delete"),
    path('view/<int:id>', views.view, name="alocacoes-view"),
]