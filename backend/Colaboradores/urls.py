from django.urls import path

from . import views

urlpatterns = [
   path('helloworld/', views.helloWorld),
   path('', views.colaboradorList, name='colaborador-list'),
   path('colaborador/<int:id>', views.colaboradorView, name="colaborador-view"),
   path('editColaborador/<int:id>', views.editColaborador, name="edit-colaborador"),
   path('novocolaborador/', views.novocolaborador, name="novo-colaborador"),
   path('deleteColaborador/<int:id>', views.deleteColaborador, name="delete-colaborador"),
]