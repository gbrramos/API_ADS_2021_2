from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from Colaboradores.models import Colaborador
from QuadroPresenca.models import QuadroPresenca

# Create your views here.
@login_required
def dash(request):
    labels = []
    data = []

    quadro = QuadroPresenca.objects.all()
    colab = Colaborador.objects.filter(tipoDeCobertura = 'fixa', situacaoCadastro = 'Ativo')
    line = []
    mat = []
    x = 0
    y = 0
    # for q in quadro:
    #     arr.append([x] * q.presenca) 
    #     x+=1

    # x = 0
    # for c in colab:
    #     arr.append([x] * c.nomeCompleto) 
    #     x+=1

    for i in range(colab.count()):
        for c in colab:
            line.append(c.nomeCompleto)
        for j in range(0,1):
             for q in quadro:
                 line.append(q.presenca)   

    mat.append(line)
    print(mat)
#    if(q.presenca == 1):
#             data.append("Presente")
#     labels.append(c.nomeCompleto)

    # print(f'data: {data}, labels:{labels}')
    return render(request, 'dashboard/index.html', {
        'data': data,
        'labels': labels,
    })