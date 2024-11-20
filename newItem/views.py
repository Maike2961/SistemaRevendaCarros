from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CadastroCarroForm
from .models import Carro
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

@login_required
def Detalhes(request, id):
    item = Carro.objects.filter(id = id).first()
    if item:
        context = {
            'item': item
        }
        return render(request, 'newItem/detalhe.html', context)
    else:
        messages.error(request, "Erro na requisição")
        return redirect('index')