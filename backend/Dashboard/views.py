from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from Colaboradores.models import Colaborador
from QuadroPresenca.models import QuadroPresenca
from QuadroPresenca.models import Dashboard
from PostosDeTrabalho.models import PostoDeTrabalho
from django.contrib import messages

# Create your views here.
@login_required
def dash(request):

    data = []
    labels = []
    faltas = 0
    multas = 0
    
    dash = Dashboard.objects.all()
    colab = Colaborador.objects.all().count()

    postos = PostoDeTrabalho.objects.all()

    for p in postos:
        colabNum = Colaborador.objects.filter(posto_id=p.id).all()
        for i in colabNum:
            faltasPosto = QuadroPresenca.objects.filter(colaboradores_id=i.id, presenca=0).count()
            faltas += faltasPosto
            if faltasPosto > p.limites_multa:
                multas += 1
     

    for d in dash:
        data.append(d.quant_presenca)
        labels.append(d.colaborador.nomeCompleto)

    return render(request, 'dashboard/index.html', {
        'data': data,
        'labels': labels,
        'numColab': colab,
        'countData': len(data),
        'start': colab + 20,
        'multas': multas
    })

@login_required
def multas(request):

    faltas = 0
    multas = 0
    contratos_multa = []

    postos = PostoDeTrabalho.objects.all()

    for p in postos:
        colabNum = Colaborador.objects.filter(posto_id=p.id).all()
        for i in colabNum:
            faltasPosto = QuadroPresenca.objects.filter(colaboradores_id=i.id, presenca=0).count()
            faltas += faltasPosto
            if faltasPosto > p.limites_multa:
                contratos_multa.append(p)
     
    return render(request, 'dashboard/multas.html', {'contratos_multa': contratos_multa})


@login_required
def colaboradores(request):
    cols = Colaborador.objects.all()
    return render(request, 'dashboard/index.html', {'cols':cols})