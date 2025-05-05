from django import forms
from .models import Juego

class JuegoForm(forms.ModelForm):
    class Meta:
        model = Juego
        fields = '__all__'  # Correcto: esto es una tupla
        # O mejor aún, lista los campos específicamente:
        # fields = ('nombre', 'precio', 'descripcion', ...)