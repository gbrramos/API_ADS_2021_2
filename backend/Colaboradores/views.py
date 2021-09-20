
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import ColaboradorForm
from django.contrib import messages

from Colaboradores.models import Colaborador

# Create your views here.

def novocolaborador(request):
    if request.method == 'POST':
        form = ColaboradorForm(request.POST)

        if form.is_valid():
            posto = form.save(commit=False)
            posto.save()
            return(redirect('../lista'))
    else:
        form = ColaboradorForm()
        return render(request, 'colaboradores/addColaborador.html', {'form':form})



def colaboradorList(request):
    colaboradores = Colaborador.objects.all().order_by('-created_at')
    return render(request, 'colaboradores/colaboradoresList.html', {'colaboradores' : colaboradores})

def colaboradorView(request, id):
    colaborador = get_object_or_404(Colaborador, pk=id)
    return render(request, 'colaboradores/colaborador.html', {'colaborador': colaborador})

def editColaborador(request, id):
    colaborador = get_object_or_404(Colaborador, pk=id)
    form = ColaboradorForm(instance=colaborador)

    if(request.method == 'POST'):
        form = ColaboradorForm(request.POST, instance=colaborador)

        if(form.is_valid()):
            colaborador.save()
            return redirect('/colaboradores')
        else:
            return render(request, 'colaboradores/editColaborador.html', {'form': form, 'colaborador': colaborador})
    else:
        return render(request, 'colaboradores/editColaborador.html', {'form': form, 'colaborador': colaborador})

def deleteColaborador(request, id):
    colaborador = get_object_or_404(Colaborador, pk=id)
    colaborador.delete()
    messages.info(request, 'Colaborador deletado com Sucesso!')
    return redirect('/colaboradores')