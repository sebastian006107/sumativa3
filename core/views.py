from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Juego
from .forms import JuegoForm, EditarUsuarioForm, RegistroForm
from django.contrib.admin.views.decorators import staff_member_required
import requests

# Create your views here.


@login_required #SEGURIDAD
def listar_juegos(request):
  juegos = Juego.objects.all()
  return render(request, "core/listar.html", {'juegos' : juegos})



@staff_member_required
@login_required
def crear_juego(request):
    form = JuegoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_juegos')
    return render(request, 'core/crear.html', {'form': form})




@staff_member_required
@login_required
def editar_juego(request, pk):
    juego = get_object_or_404(Juego, pk=pk)
    form = JuegoForm(request.POST or None, instance=juego)
    if form.is_valid():
        form.save()
        return redirect('listar_juegos')
    return render(request, 'core/editar.html', {'form': form})



@staff_member_required
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






#apirest

# apirest
from rest_framework import generics
from .models import Juego
from .serializers import JuegoSerializer

class JuegoListCreateAPIView(generics.ListCreateAPIView):
    queryset = Juego.objects.all()
    serializer_class = JuegoSerializer




class JuegoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Juego.objects.all()
    serializer_class = JuegoSerializer







    #CONSUMIR APIS
@login_required
def ofertas_view(request):
    """
    Vista que consume una API externa para mostrar ofertas de juegos.
    Requiere inicio de sesión.
    """
    try:

        api_url = "https://www.cheapshark.com/api/1.0/deals?storeID=1&upperPrice=15"
        response = requests.get(api_url, timeout=10)
        
        if response.status_code == 200:
            ofertas = response.json()
            
            ofertas = ofertas[:10] if len(ofertas) > 10 else ofertas
            
            context = {
                'ofertas': ofertas,
                'titulo': 'Ofertas Especiales'
            }
        else:
            context = {
                'error': f'Error al obtener ofertas: {response.status_code}',
                'titulo': 'Ofertas Especiales'
            }
    except requests.exceptions.RequestException as e:
        context = {
            'error': f'No se pudo conectar a la API: {str(e)}',
            'titulo': 'Ofertas Especiales'
        }
    
    return render(request, 'core/ofertas.html', context)