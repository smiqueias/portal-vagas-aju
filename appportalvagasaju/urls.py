from django.urls import path
from appportalvagasaju import views

urlpatterns = [
    path('cadastrar-vaga', views.register_job, name='cadastrar-vaga'),
    path('home', views.home, name='home'),
    path('login', views.login_usuario, name='login'),
    path('cadastrar', views.cadastrar_usuario, name='cadastrar'),
    
    

]
