from django.shortcuts import redirect, render
from django.views.generic.edit import UpdateView, DeleteView
from .forms import RegisterJobForm
from .models import Job
from django.contrib.auth.models import User
from django.contrib import auth


def register_job(request):
    pass #
    
def job_list(request):
    jobs = Job.objects.all()
    return render(request,'register_job.html',context = {'jobs':  jobs})

def home(request):
    return render(request, 'tela_inicial.html')

def login_usuario(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')

        autentificar_usuario = auth.authenticate(request, usuario,senha)

        if autentificar_usuario == None:
            return render(request, 'login_usuario.html')
        else:
            auth.login(request,autentificar_usuario)
    
def cadastrar_usuario(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar-senha')
        email = request.POST.get('email')

        user = User.objects.create_user(username=usuario,password=senha,email=email) 
        user.save()
        return redirect('home')
    return render(request, 'cadastrar_usuario.html')    

    