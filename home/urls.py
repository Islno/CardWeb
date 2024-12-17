from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('categoria/lista', views.categoria, name="lista"),
    path('categoria/formulario', views.form_categoria, name='form_categoria'),
    path('categoria/detalhe_categoria/<int:id>', views.detalhe_categoria, name='detalhe_categoria'),
    path('categoria/editar_categoria/<int:id>/', views.editar_categoria, name='editar_categoria'),
    path('categoria/delete_categoria/<int:id>/', views.delete_categoria, name='delete_categoria'),
    path('cliente/formulario', views.form_cliente, name='form_cliente'),  # URL para o formulário de Cliente
]