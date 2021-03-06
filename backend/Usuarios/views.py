from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import UsuariosForm
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.contrib.auth.hashers import make_password
from .models import Usuarios

# Create your views here.
@login_required
def novo(request):
    if request.method == 'POST':
        form = UsuariosForm(request.POST)
        if form.is_valid():
            # user = form.save()
            username = request.POST['username']
            password = request.POST['password']
            if form.data['perfil'] == 'Tatico':
                group = Group.objects.get(name='Tatico')
            else:
                group = Group.objects.get(name='Operacional')
            user = User.objects.create_user(username, password=password)
            user.is_superuser=True
            user.is_staff=True
            user.groups.add(group)
            user.save()
            return(redirect('../lista'))
    else:
        form = UsuariosForm()
        return render(request, 'usuarios/novo.html', {'form':form})

@login_required
def lista(request):
        #Search
    search = request.GET.get('search')

    if search:
        user = User.objects.filter(username__icontains=search)
    else:
        user = User.objects.all()
    return render(request, 'usuarios/lista.html', {'usuarios' : user})

@login_required
def editar(request, id):
    user = get_object_or_404(User, pk=id)
    form = UsuariosForm(instance=user)

    if(request.method == 'POST'):

        form = UsuariosForm(request.POST, instance=user)
        if(form.is_valid()):
            User.objects.filter(pk=id).update(username=request.POST['username'])
            User.objects.filter(pk=id).update(password=make_password(request.POST['password']))
            User.objects.filter(pk=id).update(email=request.POST['email'])
            if request.POST['is_superuser'] == 'on':
                User.objects.filter(pk=id).update(is_superuser=True)
            else:
                User.objects.filter(pk=id).update(is_superuser=False)
            return redirect('/usuarios/lista')
        else:
            return render(request, 'usuarios/editar.html', {'form': form, 'usuarios': user})
    else:
        return render(request, 'usuarios/editar.html', {'form': form, 'usuarios': user})

@login_required
def view(request, id):
    user = get_object_or_404(User, pk=id)
    return render(request, 'usuarios/view.html', {'user': user})

@login_required
def delete(request, id):
    user = get_object_or_404(User, pk=id)
    user.delete()
    messages.info(request, 'Usu??rio deletado com Sucesso!')
    return redirect('/usuarios/lista')