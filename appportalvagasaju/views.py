from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.edit import UpdateView, DeleteView
from .forms import RegisterJobForm
from .models import Job
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.core.validators import validate_email

@login_required(login_url='login')
def cadastrar_vaga(request):
    form = RegisterJobForm()
    contexto = {
        'form': form
    }
    return render(request,'cadastrar_vaga.html',contexto)

def home(request):
    jobs = Job.objects.all()
    return render(request,'tela_inicial.html',context = {'jobs':  jobs})

def login_usuario(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        
        usuario = auth.authenticate(request,username=usuario,password=senha)

        if usuario == None:
            messages.error(request, 'Não foi possível validar seu acesso. Tente novamente')
            return render(request, 'login.html')
        else:
            auth.login(request,usuario)
            return redirect('home')
            
    return render(request,'login.html')

@login_required
def sair(request):
    logout(request)
    return redirect('login')
    
def cadastrar_usuario(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar-senha')
        email = request.POST.get('email')
        
        if senha != confirmar_senha:
            messages.error(request,'Senhas não conferem. Tente Novamente.')
            return render(request,'cadastro.html')
        elif User.objects.filter(email=email).exists():
            messages.error(request,'Email já cadastrado')
            return render(request,'cadastro.html')
        try:
            validate_email(email)
        except:
            messages.error(request,'Insira um email válido. Ex: laura@gmail.com')
            return render(request,'cadastro.html')
        
        user = User.objects.create_user(username=usuario,password=senha,email=email) 
        user.save()
        messages.success(request,'Conta criada com sucesso!')
        return render(request,'cadastro.html')

    return render(request, 'cadastro.html')    

def detalhes_vaga(request,id):
    vaga = get_object_or_404(Job,id=id)
    contexto = {
        'vaga': vaga
    }
    return render(request,'detalhes_vaga.html',contexto)    