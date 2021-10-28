from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import UsuariosForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Usuarios

# Create your views here.
@login_required
def novo(request):
    if request.method == 'POST':
        form = UsuariosForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            if(user.perfil == "Tático"): 
                superuser = User.objects.create_superuser(
                    username=user.nome,
                    email=user.username,
                    password=user.password,
                    is_staff=1
                )
            else:
                superuser = User.objects.create_superuser(
                    username=user.nome,
                    email=user.username,
                    password=user.password,
                    is_staff=0
                )
            superuser.save()
            return(redirect('../lista'))
    else:
        form = UsuariosForm()
        return render(request, 'usuarios/novo.html', {'form':form})

@login_required
def lista(request):
    user = Usuarios.objects.all()
    return render(request, 'usuarios/lista.html', {'usuarios' : user})

@login_required
def editar(request, id):
    user = get_object_or_404(Usuarios, pk=id)
    form = UsuariosForm(instance=user)

    if(request.method == 'POST'):
        form = UsuariosForm(request.POST, instance=user)

        if(form.is_valid()):
            user.save()
            return redirect('/usuarios/lista')
        else:
            return render(request, 'usuarios/editar.html', {'form': form, 'usuarios': user})
    else:
        return render(request, 'usuarios/editar.html', {'form': form, 'usuarios': user})

@login_required
def view(request, id):
    user = get_object_or_404(Usuarios, pk=id)
    return render(request, 'usuarios/view.html', {'user': user})

@login_required
def delete(request, id):
    user = get_object_or_404(Usuarios, pk=id)
    user.delete()
    messages.info(request, 'Usuário deletado com Sucesso!')
    return redirect('/usuarios/lista')