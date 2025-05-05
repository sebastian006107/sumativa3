from rest_framework import serializers
from .models import Juego
from rest_framework import generics


class JuegoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Juego
        fields = '__all__' 


