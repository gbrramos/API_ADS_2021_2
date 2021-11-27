from django.urls import path

from . import views

urlpatterns = [
    path('', views.dash, name='dash'),
    path('', views.colaboradores, name='cols'),
    path('multas', views.multas, name='dash')
]