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
    arrData = data.split('/')
    sqlData = Data(dia=arrData[0], month=arrData[1], ano=arrData[2])
    sqlData.save()
    for i in id_cols:
        
        presenca = request.POST.get(f'presenca_{i.id}')
        last_data = Data.objects.all().order_by('-id').first()
        
        if presenca is None:
            presenca = False
        #sqlQuadro = Registra primeiro a tabela quadropresenca_quadropresenca    
        sqlQuadro = QuadroPresenca(presenca=presenca, colaboradores_id=i.id)
        sqlQuadro.save()
        #dataQuadro recebe o id setado no input
        dataQuadro = sqlQuadro.id
        #quadro recebe essa data e o comando add cria o relacionamento na tabela quadropresenca_quadropresenca_data
        #quadro possui = id do colaborador, presenca, id do quadro
        #quadro com esses dados + a insercao do campo id_data
        quadro = QuadroPresenca.objects.get(id=dataQuadro)
        quadro.data_id.add(sqlData.id)

    return redirect('../novaData/10')
 
#ainda nao estao sendo usadas
# def viewQuadro(request,id):
#     quadro = get_list_or_404(QuadroPresenca,pk=id)
#     return render(request, 'quadrodepresenca/viewQuadro.html', {'quadro': quadro})

def view_quadros(request,id):
    posto = PostoDeTrabalho.objects.filter(id=id)
    quadro = QuadroPresenca.objects.order_by('-id').first()
    data = Data.objects.all().order_by('-id').first()
    cols = Colaborador.objects.filter(posto_id=id)
    dataQuadro = quadro.data_id.all()
    diaMes = Data.objects.filter(month=data.month)
    colabQuadro = QuadroPresenca.objects.filter(data_id=data.id)
    colaboradores = Colaborador.objects.all()
    presencas = QuadroPresenca.objects.all()
    for q in colabQuadro:
        print(q.id)
        print(q.presenca)
    

    return render(request, 'quadrodepresenca/viewQuadro.html', {'colaboradores': colaboradores, 'datas': data, 'dias': diaMes, 'quadro': colabQuadro, 'presencas': presencas})
#        for q in quadro:
#            dia.append(q.presenca)
#        matrizPresenca.append(dia)
#    print(matrizPresenca)
#    for l in range(countDia):
#        for c in range(countQuadros):
#            print(matrizPresenca[l][c])
#        print('-'*30)
        