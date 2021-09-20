from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import QuadroDePresencaForm
from django.contrib import messages

from .models import QuadroDePresenca
from PostosDeTrabalho.models import PostoDeTrabalho

# Create your views here.

def novo(request):
    if request.method == 'POST':
        form = QuadroDePresencaForm(request.POST)

        if form.is_valid():
            posto = form.save(commit=False)
            posto.save()
            return(redirect('../lista'))
    else:
        form = QuadroDePresencaForm()
        return render(request, 'postosdetrabalho/novo.html', {'form':form})



def lista(request):
    count = PostoDeTrabalho.objects.count()
    quadros = PostoDeTrabalho.objects.all()
    print(quadros)
    return render(request, 'quadrodepresenca/lista.html', {'quadros' : quadros})

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