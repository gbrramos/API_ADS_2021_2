from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import ContratosForms
from django.contrib import messages

from .models import Contrato

# Create your views here.

def novo(request):
    if request.method == 'POST':
        form = ContratosForms(request.POST)

        if form.is_valid():
            posto = form.save(commit=False)
            posto.save()
            return(redirect('../lista'))
    else:
        form = ContratosForms()
        return render(request, 'contratos/novo.html', {'form':form})



def lista(request):
    contratos = Contrato.objects.all()
    return render(request, 'contratos/contratosList.html', {'contratos' : contratos})

def edit(request, id):
    contrato = get_object_or_404(Contrato, pk=id)
    form = ContratosForms(instance=contrato)

    if(request.method == 'POST'):
        form = ContratosForms(request.POST, instance=contrato)

        if(form.is_valid()):
            contrato.save()
            return redirect('/contratos/lista')
        else:
            return render(request, 'contratos/editar.html', {'form': form, 'contrato': contrato})
    else:
        return render(request, 'contratos/editar.html', {'form': form, 'contrato': contrato})

def view(request, id):
    contrato = get_object_or_404(Contrato, pk=id)
    return render(request, 'contratos/view.html', {'contrato': contrato})


def delete(request, id):
    contrato = get_object_or_404(Contrato, pk=id)
    contrato.delete()
    messages.info(request, 'Contrato deletado com Sucesso!')
    return redirect('/contratos/lista')