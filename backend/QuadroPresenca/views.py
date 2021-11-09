import django
from django.core.exceptions import DisallowedHost
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.http import HttpResponse
from Alocacoes.forms import AlocacoesForms
from django.contrib.auth.decorators import login_required
from Colaboradores.views import colaboradorList
from .forms import QuadroDePresencaForm, DataForm
from django.contrib import messages
from django.views.generic.list import ListView
from .models import Data, QuadroPresenca, Dashboard
from PostosDeTrabalho.models import PostoDeTrabalho
from Colaboradores.models import Colaborador
from Alocacoes.models import Alocacao
from django.template.response import TemplateResponse
from django.db import connection
from collections import namedtuple

# Create your views here.

@login_required
def lista(request):
    count = PostoDeTrabalho.objects.count()
    form = DataForm(request.POST)
    postos = PostoDeTrabalho.objects.all()
    count = len(postos)
    return render(request, 'quadrodepresenca/lista.html', {'postos' : postos, 'form': form, 'count': count})


@login_required
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

@login_required
def aprovarQuadro(request, id):
    quadro = get_object_or_404(QuadroPresenca, pk=id)
    quadro.update(is_approved=True)
    return redirect('/postosTrabalho/lista')


@login_required
def view(request, id):
    posto = get_object_or_404(QuadroPresenca, pk=id)
    return render(request, 'postosdetrabalho/view.html', {'posto': posto})

@login_required
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



@login_required
def novaData(request,id):
    data = DataForm(request.POST)
    postos = PostoDeTrabalho.objects.filter(id=id).first()
    flutuante = Colaborador.objects.filter(tipoDeCobertura='flutuante')
    col = Colaborador.objects.filter(posto_id=id,tipoDeCobertura='fixa')
    form = DataForm(request.POST)
    alocacao = Alocacao.objects.all()
    return TemplateResponse(request, 'quadrodepresenca/novo.html', {'cols': col, 'postos': postos, 'data': data, 'flutuante': flutuante})

@login_required
def storeData(request, id):
    maximo_colaboradores = Colaborador.objects.filter(posto_id=id).count()

    id_cols = Colaborador.objects.filter(posto_id=id,tipoDeCobertura='fixa')
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
    dash = Dashboard.objects.all()
    cDash = len(dash)
    sqlDash = []
    if cDash >= 1:
        for i in id_cols:
            # Erro abaixo - Cadastra dois
            if i.id in dash.colaborador.id:
                d = Dashboard.objects.get(colaborador=i)
                
                presenca = request.POST.get(f'presenca_{i.id}')
                if presenca is not None:
                    quant = d.quant_presenca
                    quant = quant + 1
                    Dashboard.objects.filter(colaborador=i).update(colaborador=i, quant_presenca=quant)
                    
            else:
                presenca = request.POST.get(f'presenca_{i.id}')
                if presenca is not None:
                    Dashboard.objects.create(colaborador=i, quant_presenca=1)
    else:
        for i in id_cols:
            presenca = request.POST.get(f'presenca_{i.id}')
            if presenca is not None:
                Dashboard.objects.create(colaborador=i, quant_presenca=1)

    return redirect('../lista')
 
#ainda nao estao sendo usadas
# def viewQuadro(request,id):
#     quadro = get_list_or_404(QuadroPresenca,pk=id)
#     return render(request, 'quadrodepresenca/viewQuadro.html', {'quadro': quadro})

@login_required
def view_quadros(request,id):
    posto = PostoDeTrabalho.objects.filter(id=id)
    quadro = QuadroPresenca.objects.order_by('-id').first()
    data = Data.objects.all().order_by('-id').first()
    cols = Colaborador.objects.filter(posto_id=id,tipoDeCobertura='fixa')
    dataQuadro = quadro.data_id.all()
    diaMes = Data.objects.filter(month=data.month)
    colabQuadro = QuadroPresenca.objects.filter(data_id=data.id)
    quadroP = QuadroPresenca.objects.all()
    colaboradores = Colaborador.objects.all()
    data = Data.objects.raw("SELECT * FROM quadropresenca_quadropresenca_data_id")
    data_id = []
    for d in data:
        data_id.append(d.quadropresenca_id)
    print(data_id)
    p = []   
    presencas = {}
    for d in diaMes:
        q = QuadroPresenca.objects.filter(data_id=d.id)
        for quadro in q:
            if quadro.presenca == True:
                p.append('P')
            if quadro.presenca == False:
                p.append('F')
    # pPerCol = int(len(p)/len(q))
    print(f'Quantidade de presencas ao longo de {len(diaMes)} dia(s) = {len(p)}')  
    print(f'Numeros de quadros por dia: {len(q)}')
    # print(pPerCol)  
    dia = len(diaMes)
    i = 0
    #Quantidade de quadros por dia
    qPerDia = len(q)
    #Caso só houver um dia registrado, as presenças são todas alocadas neste dia
    if len(diaMes) == 1:
        for d in diaMes:
            presencas[d.dia] = p
    else:
    #Caso haja mais de um dia, as presencas são alocadas por dia
        #Para cada dia no mes:
        for d in cols:
            #Em cada chave do dicionario(que são representadas em dia), registra as Presencas/Faltas dos colaboradores no dia
            presencas[int(d.id)] = p[i:qPerDia]
            # a cada dia a variavel "i"(que inicia em zero) recebe a posicao da ultima presenca registrada
            i = qPerDia
            # a variavel "qPerdia" recebe qPerdia + a quantidade de quadros por dia
            qPerDia+=len(q)
    # print(presencas)
   
    colabIds = []
    for colab in cols:
        colabIds.append(colab.id)
    print(quadroP.values())

    return render(request, 'quadrodepresenca/viewQuadro.html', {'colaboradores': cols, 'presencas': quadroP, 'dia': diaMes, 'data_id': data_id, 'posto':posto})
#        for q in quadro:
#            dia.append(q.presenca)
#        matrizPresenca.append(dia)
#    print(matrizPresenca)
#    for l in range(countDia):
#        for c in range(countQuadros):
#            print(matrizPresenca[l][c])
#        print('-'*30)

@login_required
def edit(request, id):
    posto = PostoDeTrabalho.objects.filter(id=id)
    quadroP = QuadroPresenca.objects.all()
    data = Data.objects.all().order_by('-id').first()
    diaMes = Data.objects.filter(month=data.month)
    data = Data.objects.raw("SELECT * FROM quadropresenca_quadropresenca_data_id")
    colaboradores = Colaborador.objects.raw('SELECT * FROM colaboradores_colaborador WHERE tipoDeCobertura = "fixa" and posto_id = %s', [id])
    return render(request, 'quadrodepresenca/editar.html', {'posto':posto, 'data':data, 'presencas': quadroP, 'colaboradores': colaboradores, 'dia': diaMes})


@login_required
def quadroGeral(request):
    id_postos = PostoDeTrabalho.objects.all()
    posto = PostoDeTrabalho.objects.all()
    quadro = QuadroPresenca.objects.all()
    dataMes = Data.objects.all().order_by('-id').first()
    data = Data.objects.raw("SELECT * FROM quadropresenca_quadropresenca_data_id")
    colaboradores = Colaborador.objects.raw('SELECT * FROM colaboradores_colaborador WHERE tipoDeCobertura = "fixa"')
    diaMes = Data.objects.filter(month=dataMes.month)

    return render(request, 'quadrodepresenca/quadroGeral.html', {'posto':posto, 'presencas': quadro, 'data':data, 'cols': colaboradores, 'id_postos': id_postos, 'dia': diaMes})
