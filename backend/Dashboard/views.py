from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from Colaboradores.models import Colaborador
from QuadroPresenca.models import QuadroPresenca
from QuadroPresenca.models import Dashboard
from django.contrib import messages

# Create your views here.
@login_required
def dash(request):

    data = []
    labels = []

    dash = Dashboard.objects.all()
    colab = Colaborador.objects.all().count()
    for d in dash:
        data.append(d.quant_presenca)
        labels.append(d.colaborador.nomeCompleto)

    return render(request, 'dashboard/index.html', {
        'data': data,
        'labels': labels,
        'numColab': colab,
        'start': colab - 20
    })


@login_required
def colaboradores(request):
    cols = Colaborador.objects.all()
    return render(request, 'dashboard/index.html', {'cols':cols})