from django.urls import path

from . import views

urlpatterns = [
    path('lista/', views.lista, name='quadro-presenca-lista'),
    path('novo/', views.novo, name="quadro-presenca-novo"),
    path('novaData/<int:id>', views.novaData, name="quadro-presenca-novaData"),
    path('storeData/<int:id>', views.storeData, name="quadro-presenca-storeData"),
    path('updateData/<int:rid>', views.updateQuadro, name="quadro-presenca-updateData"),
    path('viewQuadros/<int:id>', views.view_quadros, name="view_quadros"),
    path('justificarFalta/<int:id>', views.justificarFalta, name="justificarFalta"),
    path('editar/<int:id>', views.edit, name="quadro-presenca-editar"),
    path('delete/<int:id>', views.delete, name="quadro-presenca-delete"),
    path('view/<int:id>', views.view, name="postos-trabalho-view"),
    path('quadroGeral/', views.quadroGeral, name="quadro-geral"),
    path('data/', views.data, name="quadro-presenca-data"),
    path('deleteData/<int:id>', views.deleteData, name="quadro-presenca-apagar-data"),
    path('justificativa/<int:id>', views.justificativa, name="quadro-presenca-justificativa"),
]