from django.shortcuts import render, redirect, get_object_or_404
from .models import Juego
from .forms import JuegoForm

# Create your views here.
def listar_juegos(request):
  juegos = Juego.objects.all()
  return render(request, "core/listar.html", {'juegos' : juegos})

def crear_juego(request):
    form = JuegoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_juegos')
    return render(request, 'core/crear.html', {'form': form})


def editar_juego(request, pk):
    juego = get_object_or_404(Juego, pk=pk)
    form = JuegoForm(request.POST or None, instance=juego)
    if form.is_valid():
        form.save()
        return redirect('listar_juegos')
    return render(request, 'core/editar.html', {'form': form})


def eliminar_juego(request, pk):
    juego = get_object_or_404(Juego, pk=pk)
    if request.method == 'POST':
        juego.delete()
        return redirect('listar_juegos')
    return render(request, 'core/eliminar.html', {'juego': juego})

