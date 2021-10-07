import django
from django.core.exceptions import DisallowedHost
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.http import HttpResponse

from Colaboradores.views import colaboradorList
from .forms import QuadroDePresencaForm, DataForm
from django.contrib import messages
from django.views.generic.list import ListView
from .models import Data, QuadroPresenca
from PostosDeTrabalho.models import PostoDeTrabalho
from Colaboradores.models import Colaborador
from django.template.response import TemplateResponse

# Create your views here.

def lista(request):
    count = PostoDeTrabalho.objects.count()
    form = DataForm(request.POST)
    postos = PostoDeTrabalho.objects.all()
    quadros = QuadroPresenca.objects.all()
    return render(request, 'quadrodepresenca/lista.html', {'postos' : postos, 'form': form})


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
    posto = get_object_or_404(QuadroPresenca, pk=id)
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
    posto = get_object_or_404(QuadroPresenca, pk=id)
    return render(request, 'postosdetrabalho/view.html', {'posto': posto})


def delete(request, id):
    posto = get_object_or_404(QuadroPresenca, pk=id)
    posto.delete()
    messages.info(request, 'Posto de Trabalho deletado com Sucesso!')
    return redirect('/postosTrabalho/lista')


#def novaData(request, id):
#    form = DataForm(request.POST)
#    col = Colaborador.objects.filter(posto_id=id)
#    if form.is_valid():
#        data = form.save(commit=False)
#        data.save()
#    return TemplateResponse(request, 'quadrodepresenca/novo.html', {'cols': col}) 

def view_quadros(request):
    quadro = get_list_or_404(QuadroPresenca)
    return render(request, 'quadrodepresenca/viewQuadro.html', {'posto': quadro})


def novaData(request,id):
    data = DataForm(request.POST)
    postos = PostoDeTrabalho.objects.filter(id=id).first()
    flutuante = Colaborador.objects.filter(tipoDeCobertura='flutuante')
    col = Colaborador.objects.filter(posto_id=id)
    form = DataForm(request.POST)
    return TemplateResponse(request, 'quadrodepresenca/novo.html', {'cols': col, 'postos': postos, 'data': data, 'flutuante': flutuante})

def storeData(request, id):
    maximo_colaboradores = Colaborador.objects.filter(posto_id=id).count()

    id_cols = Colaborador.objects.filter(posto_id=id)
    data = request.POST.get('data')
    sqlData = Data(data=data)
    sqlData.save()
    for i in id_cols:
        
        presenca = request.POST.get(f'presenca_{i.id}')
        last_data = Data.objects.all().order_by('-id').first()
        
        if presenca is None:
            presenca = False    

        sqlQuadro = QuadroPresenca(presenca=presenca, colaboradores_id=i.id)
        sqlData = Data.data_set.all()
        sqlQuadro.save()
        sqlData.save()
        
    return redirect('../novaData/10')
 

# def cadastra_presenca(request):
#     if 'valor_da_presenca' in request.POST:
#             presenca = request.POST['valor_da_presenca']
#     else:
#             presenca = False
#     colaborador = Colaborador.objects.all()
#     quadro = get_object_or_404(QuadroPresenca,pk=id)
#     return TemplateResponse(request,'quadrodepresenca/viewQuadro.html', {'colaborador': colaborador, 'quadro':quadro})
