from django.urls import path

from . import views

urlpatterns = [
    path('lista', views.lista, name='contratos-lista'),
    path('novo/', views.novo, name="contratos-novo"),
    path('editar/<int:id>', views.edit, name="contratos-editar"),
    path('delete/<int:id>', views.delete, name="contratos-delete"),
    path('view/<int:id>', views.view, name="contratos-view"),
    path('gerarRelatorio/<int:id>', views.gerarRelatorio, name="gerar-relatorio"),
]