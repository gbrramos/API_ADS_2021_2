from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import AlocacoesForms
from django.contrib import messages

from .models import Alocacao

# Create your views here.

def novo(request):
    if request.method == 'POST':
        form = AlocacoesForms(request.POST)

        if form.is_valid():
            posto = form.save(commit=False)
            posto.save()
            return(redirect('../lista'))
    else:
        form = AlocacoesForms()
        return render(request, 'contratos/novo.html', {'form':form})



def lista(request):
    contratos = Alocacao.objects.all()
    return render(request, 'alocacoes/lista.html', {'contratos' : contratos})

def edit(request, id):
    contrato = get_object_or_404(Alocacao, pk=id)
    form = AlocacoesForms(instance=contrato)

    if(request.method == 'POST'):
        form = AlocacoesForms(request.POST, instance=contrato)

        if(form.is_valid()):
            contrato.save()
            return redirect('/contratos/lista')
        else:
            return render(request, 'contratos/editar.html', {'form': form, 'contrato': contrato})
    else:
        return render(request, 'contratos/editar.html', {'form': form, 'contrato': contrato})

def view(request, id):
    contrato = get_object_or_404(Alocacao, pk=id)
    return render(request, 'contratos/view.html', {'contrato': contrato})


def delete(request, id):
    contrato = get_object_or_404(Alocacao, pk=id)
    contrato.delete()
    messages.info(request, 'Contrato deletado com Sucesso!')
    return redirect('/contratos/lista')