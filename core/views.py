from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Juego
from .forms import JuegoForm

# Create your views here.


@login_required #SEGURIDAD
def listar_juegos(request):
  juegos = Juego.objects.all()
  return render(request, "core/listar.html", {'juegos' : juegos})


@login_required
def crear_juego(request):
    form = JuegoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_juegos')
    return render(request, 'core/crear.html', {'form': form})


@login_required
def editar_juego(request, pk):
    juego = get_object_or_404(Juego, pk=pk)
    form = JuegoForm(request.POST or None, instance=juego)
    if form.is_valid():
        form.save()
        return redirect('listar_juegos')
    return render(request, 'core/editar.html', {'form': form})

@login_required
def eliminar_juego(request, pk):
    juego = get_object_or_404(Juego, pk=pk)
    if request.method == 'POST':
        juego.delete()
        return redirect('listar_juegos')
    return render(request, 'core/eliminar.html', {'juego': juego})














from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('listar_juegos')
    else:
        form = RegistroForm()
    return render(request, 'core/registro.html', {'form': form})







@login_required
def editar_perfil(request):
    if request.method == 'POST':
        form = EditarUsuarioForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)

            password = form.cleaned_data.get('password1')
            if password:
                user.set_password(password)

            user.save()
            return redirect('login')  
    else:
        form = EditarUsuarioForm(instance=request.user)

    return render(request, 'core/editar_perfil.html', {'form': form})



