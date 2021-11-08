from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import ContratosForms
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from io import StringIO
from io import BytesIO
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from html import escape
from QuadroPresenca.models import QuadroPresenca
from PostosDeTrabalho.models import PostoDeTrabalho
from QuadroPresenca.models import Data, QuadroPresenca
from Colaboradores.models import Colaborador
from .models import Contrato

# Create your views here.
@login_required
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


@login_required
def lista(request):
    contratos = Contrato.objects.all()
    return render(request, 'contratos/contratosList.html', {'contratos' : contratos})

@login_required
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

@login_required
def view(request, id):
    contrato = get_object_or_404(Contrato, pk=id)
    return render(request, 'contratos/view.html', {'contrato': contrato})

@login_required
def delete(request, id):
    contrato = get_object_or_404(Contrato, pk=id)
    contrato.delete()
    messages.info(request, 'Contrato deletado com Sucesso!')
    return redirect('/contratos/lista')


# @login_required
# def gerarRelatorio(request):
#     # Create Bytestream buffer
#     buf = io.BytesIO()
#     # Create a canvas
#     c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
#     # Create a text object
#     textob = c.beginText()
#     textob.setTextOrigin(inch, inch)
#     textob.setFont("Helvetica", 14)
#     #Dados do Contrato

#     #Add some lines of text
#     lines = [
#         "Guilherme",
#         "Felipe",
#         "Eduardo",
#     ]

#     for line in lines:
#         textob.textLine(line)

#     c.drawText(textob)
#     c.showPage()
#     c.save()
#     buf.seek(0)
#     return FileResponse(buf, as_attachment=True, filename='relatorio.pdf')

@login_required
def gerarRelatorio(request, id):
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

    #Retrieve data or whatever you need
    contrato = get_object_or_404(Contrato, pk=id)
    print(f"Request: {contrato}")
    return render_to_pdf(
            'contratos/pdf.html',
            {
                'pagesize':'A4',
                'contrato': contrato,
                'colaboradores': cols,
                'presencas': quadroP, 
                'dia': diaMes, 
                'data_id': data_id
            }
        )


def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    # context = Context(context_dict)
    html  = template.render(context_dict)
    result = BytesIO()

    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))