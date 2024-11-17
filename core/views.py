from django.shortcuts import render, redirect
from .forms import CadastroForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout


@login_required
def index(request):
    print(request.user)
    return render(request, "core/index.html")

def login(request):
    print(request.user)
    return render(request, "core/login.html")

def logout(request):
    auth_logout(request)
    return redirect('login')

def cadastro(request):
    if request.method == "POST":
        form = CadastroForm(request.POST)
        if form.is_valid():
            form.save()
            print("Correto")
            return redirect('login')
        else:
            print(form.error_messages)
    else:
        form = CadastroForm()
    context = {'form': form}
    return render(request, 'core/cadastro.html', context)
