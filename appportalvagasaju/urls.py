from django.urls import path
from appportalvagasaju import views

urlpatterns = [
    path('cadastrar-vaga', views.cadastrar_vaga, name='cadastrar-vaga'),
    path('', views.home, name='home'),
    path('login', views.login_usuario, name='login'),
    path('cadastro', views.cadastrar_usuario, name='cadastro'),
    path('sair', views.sair, name='sair'),
    path('cadastrar', views.cadastrar_usuario, name='cadastrar'),
    path('vaga/<int:id>', views.detalhes_vaga, name='detalhes-vaga'),

]
