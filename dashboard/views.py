from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from newItem.models import Carro
from django.contrib import messages
from .forms import editarCarroForm


@login_required
def dashboard(request):
    item = Carro.objects.filter(criado_por = request.user).first()
    context = {
        'item': item
    }
    return render(request, 'dashboard.html', context)


@login_required
def editar(request, id):
    item = Carro.objects.get(id=id)
    if request.method == "POST":
        form = editarCarroForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()
            messages.success(request, 'Item Editado com sucesso')
            return redirect("dashboard:dashboard")
    else:
        form = editarCarroForm(instance=item)
    
    context = {
        'form': form
    }
    return render(request, 'formsEditar.html', context)

@login_required
def delete(request, id):
    item = Carro.objects.get(id=id)
    if item:
        item.delete()
        messages.success(request, 'Excluido com sucesso')
    else:
        messages.error(request, 'Erro ao Excluir')
    return redirect("dashboard:dashboard")
        
