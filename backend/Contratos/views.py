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
    #Retrieve data or whatever you need
    contrato = get_object_or_404(Contrato, pk=id)
    print(f"Request: {contrato}")
    return render_to_pdf(
            'contratos/model.html',
            {
                'pagesize':'A4',
                'contrato': contrato,
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