from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import AlocacoesForms
from django.contrib import messages
from Colaboradores.models import Colaborador
from PostosDeTrabalho.models import PostoDeTrabalho
from .models import Alocacao
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def novo(request):
    if request.method == 'POST':
        form = AlocacoesForms(request.POST)

        if form.is_valid():
            posto = form.save(commit=False)
            posto.save()
            return(redirect('../lista'))
    else:
        # colabs = Colaborador.objects.filter(tipoDeCobertura='flutuante')
        # postos = PostoDeTrabalho.objects.all()
        form = AlocacoesForms()
        # return render(request, 'alocacoes/novo.html', {'colabs':colabs,'postos': postos})
        return render(request, 'alocacoes/novo.html', {'form':form})

@login_required
def lista(request):
    alocacoes = Alocacao.objects.all()
    return render(request, 'alocacoes/lista.html', {'alocacoes' : alocacoes})

@login_required
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

@login_required
def view(request, id):
    contrato = get_object_or_404(Alocacao, pk=id)
    return render(request, 'contratos/view.html', {'contrato': contrato})

@login_required
def delete(request, id):
    contrato = get_object_or_404(Alocacao, pk=id)
    contrato.delete()
    messages.info(request, 'Alocação deletado com Sucesso!')
    return redirect('/alocacoes/lista')