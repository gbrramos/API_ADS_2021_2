import django
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.http import HttpResponse
from .forms import QuadroDePresencaForm, DataForm
from django.contrib import messages
from django.views.generic.list import ListView
from .models import QuadroDePresenca
from PostosDeTrabalho.models import PostoDeTrabalho
from Colaboradores.models import Colaborador
from django.template.response import TemplateResponse

# Create your views here.

def lista(request):
    count = PostoDeTrabalho.objects.count()
    form = DataForm(request.POST)
    postos = PostoDeTrabalho.objects.all()
    quadros = QuadroDePresenca.objects.all()
    return render(request, 'quadrodepresenca/lista.html', {'postos' : postos, 'form': form})

def novaData(request, id):
    form = DataForm(request.POST)
    col = Colaborador.objects.filter(posto_id=id)
    if form.is_valid():
        data = form.save(commit=False)
        data.save()
        return TemplateResponse(request, 'quadrodepresenca/novo.html', {'cols': col})

def viewQuadro(request):
    col = Colaborador.objects.all()
    return render(request, 'quadrodepresenca/viewQuadro.html', {'cols': col})
    
def novo(request):
    if request.method == 'POST':
        form = QuadroDePresencaForm(request.POST)

        if form.is_valid():
            posto = form.save(commit=False)
            posto.save()
            return(redirect('../lista'))
    else:
        form = QuadroDePresencaForm()
        return render(request, 'quadrodepresenca/novo.html', {'form':form})


def edit(request, id):
    posto = get_object_or_404(QuadroDePresenca, pk=id)
    form = QuadroDePresencaForm(instance=posto)

    if(request.method == 'POST'):
        form = QuadroDePresencaForm(request.POST, instance=posto)

        if(form.is_valid()):
            posto.save()
            return redirect('/postosTrabalho/lista')
        else:
            return render(request, 'postosdetrabalho/editar.html', {'form': form, 'posto': posto})
    else:
        return render(request, 'postosdetrabalho/editar.html', {'form': form, 'posto': posto})

def view(request, id):
    posto = get_object_or_404(QuadroDePresenca, pk=id)
    return render(request, 'postosdetrabalho/view.html', {'posto': posto})


def delete(request, id):
    posto = get_object_or_404(QuadroDePresenca, pk=id)
    posto.delete()
    messages.info(request, 'Posto de Trabalho deletado com Sucesso!')
    return redirect('/postosTrabalho/lista')