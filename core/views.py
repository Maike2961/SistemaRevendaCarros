from django.shortcuts import render, redirect
from .forms import CadastroForm, FiltroMarcaForm
from newItem.models import Carro
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout


@login_required
def index(request):
    form = FiltroMarcaForm(request.GET or None)
    item = Carro.objects.all()
    if form.is_valid():
        marca = form.cleaned_data.get('Pesquisa')
        if marca:
            item = item.filter(nome__icontains=marca)
            
    items_agrupado = (item.values('marca_carro__marca_carro').annotate(count=Count('marca_carro')).order_by('marca_carro__marca_carro'))
    print(items_agrupado)
    context = {
        'item': item,
        'form': form,
        'items_agrupado': items_agrupado
    }
    return render(request, "core/index.html", context)

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
