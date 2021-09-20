from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import PostosDeTrabalhoForms
from django.contrib import messages

from .models import PostoDeTrabalho

# Create your views here.

def novo(request):
    if request.method == 'POST':
        form = PostosDeTrabalhoForms(request.POST)

        if form.is_valid():
            posto = form.save(commit=False)
            posto.save()
            return(redirect('../lista'))
    else:
        form = PostosDeTrabalhoForms()
        return render(request, 'postosdetrabalho/novo.html', {'form':form})



def lista(request):
    postos = PostoDeTrabalho.objects.all().order_by('-created_at')
    return render(request, 'postosdetrabalho/postosTrabalhoList.html', {'postos' : postos})

def edit(request, id):
    posto = get_object_or_404(PostoDeTrabalho, pk=id)
    form = PostosDeTrabalhoForms(instance=posto)

    if(request.method == 'POST'):
        form = PostosDeTrabalhoForms(request.POST, instance=posto)

        if(form.is_valid()):
            posto.save()
            return redirect('/postosTrabalho/lista')
        else:
            return render(request, 'postosdetrabalho/editar.html', {'form': form, 'posto': posto})
    else:
        return render(request, 'postosdetrabalho/editar.html', {'form': form, 'posto': posto})

def view(request, id):
    posto = get_object_or_404(PostoDeTrabalho, pk=id)
    return render(request, 'postosdetrabalho/view.html', {'posto': posto})


def delete(request, id):
    posto = get_object_or_404(PostoDeTrabalho, pk=id)
    posto.delete()
    messages.info(request, 'Posto de Trabalho deletado com Sucesso!')
    return redirect('/postosTrabalho/lista')