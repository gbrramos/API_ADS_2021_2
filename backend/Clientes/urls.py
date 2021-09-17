from django.urls import path

from . import views

urlpatterns = [
   path('lista', views.lista, name='cliente-list'),
   path('cliente/<int:id>', views.view, name="cliente-view"),
   path('editar/<int:id>', views.editar, name="edit-cliente"),
   path('novo/', views.novo, name="novo-cliente"),
   path('delete/<int:id>', views.delete, name="delete-cliente"),
]