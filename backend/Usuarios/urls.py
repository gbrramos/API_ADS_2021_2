from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('lista', views.lista, name='usuarios-lista'),
    path('login/', auth_views.LoginView.as_view(
        template_name='usuarios/login.html'
    ), name='login'),
    path('novo/', views.novo, name="usuarios-novo"),
    path('editar/<int:id>', views.editar, name="usuarios-editar"),
    path('delete/<int:id>', views.delete, name="usuarios-delete"),
    path('view/<int:id>', views.view, name="usuarios-view"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]