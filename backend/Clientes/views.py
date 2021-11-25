from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import ClientesForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from .models import Clientes

# Create your views here.
@login_required
def novo(request):
    if request.method == 'POST':
        form = ClientesForm(request.POST)

        if form.is_valid():
            posto = form.save(commit=False)
            posto.save()
            return(redirect('../lista'))
    else:
        form = ClientesForm()
        return render(request, 'clientes/novo.html', {'form':form})
@login_required
def store(request):
    if request.method == 'POST':
        form = ClientesForm(request.POST)

        if form.is_valid():
            cli = form.save(commit=False)
            cli.tipoDeCobertura = 'fixa'
            cli.save()
            return(redirect('/lista'))
    else:
        form = ClientesForm()
        return render(request, 'clientes/novo.html', {'form':form})

@login_required
def lista(request):
        #Search
    search = request.GET.get('search')

    if search:
        clientes = Clientes.objects.filter(nome_fantasia__icontains=search)
    else:
        clientes = Clientes.objects.all()
    return render(request, 'clientes/lista.html', {'clientes' : clientes})

@login_required
def editar(request, id):
    cli = get_object_or_404(Clientes, pk=id)
    form = ClientesForm(instance=cli)

    if(request.method == 'POST'):
        form = ClientesForm(request.POST, instance=cli)

        if(form.is_valid()):
            cli.save()
            return redirect('/clientes/lista')
        else:
            return render(request, 'clientes/editar.html', {'form': form, 'cliente': cli})
    else:
        return render(request, 'clientes/editar.html', {'form': form, 'cliente': cli})

@login_required
def view(request, id):
    cliente = get_object_or_404(Clientes, pk=id)
    return render(request, 'clientes/view.html', {'cliente': cliente})

@login_required
def delete(request, id):
    cli = get_object_or_404(Clientes, pk=id)
    cli.delete()
    messages.info(request, 'Clientes deletado com Sucesso!')
    return redirect('/clientes/lista')