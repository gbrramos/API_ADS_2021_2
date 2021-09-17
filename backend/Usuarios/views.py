from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import UsuariosForm
from django.contrib import messages

from .models import Usuarios

# Create your views here.

def novo(request):
    if request.method == 'POST':
        form = UsuariosForm(request.POST)

        if form.is_valid():
            posto = form.save(commit=False)
            posto.save()
            return(redirect('../lista'))
    else:
        form = UsuariosForm()
        return render(request, 'usuarios/novo.html', {'form':form})

def store(request):
    if request.method == 'POST':
        form = UsuariosForm(request.POST)

        if form.is_valid():
            cli = form.save(commit=False)
            cli.tipoDeCobertura = 'fixa'
            cli.save()
            return(redirect('/lista'))
    else:
        form = UsuariosForm()
        return render(request, 'usuarios/novo.html', {'form':form})

def lista(request):
    clis = Usuarios.objects.all().order_by('-created_at')
    return render(request, 'usuarios/lista.html', {'usuarios' : clis})

def editar(request, id):
    cli = get_object_or_404(Usuarios, pk=id)
    form = UsuariosForm(instance=cli)

    if(request.method == 'POST'):
        form = UsuariosForm(request.POST, instance=cli)

        if(form.is_valid()):
            cli.save()
            return redirect('/usuarios/lista')
        else:
            return render(request, 'usuarios/editar.html', {'form': form, 'usuarios': cli})
    else:
        return render(request, 'usuarios/editar.html', {'form': form, 'usuarios': cli})

def view(request, id):
    posto = get_object_or_404(Usuarios, pk=id)
    return render(request, 'postosdetrabalho/view.html', {'posto': posto})


def delete(request, id):
    cli = get_object_or_404(Usuarios, pk=id)
    cli.delete()
    messages.info(request, 'Usuário deletado com Sucesso!')
    return redirect('/usuarios/lista')