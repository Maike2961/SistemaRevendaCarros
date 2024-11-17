from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CadastroCarroForm
from django.contrib.auth.decorators import login_required


@login_required
def CadastroNovoCarro(request):
    if request.method == "POST":
        form = CadastroCarroForm(request.POST, request.FILES)
        if form.is_valid():
            carro = form.save(commit=False)
            carro.criado_por = request.user
            carro.save()
            messages.success(request, 'Cadastrado com Sucesso')
            return redirect('index')
        else:
            print(form.errors)
    else:
        form = CadastroCarroForm()
    
    context = {
        'form': form
    }
    return render(request, "newItem/cadastroItem.html", context)