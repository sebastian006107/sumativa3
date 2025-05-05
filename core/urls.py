from django.urls import path
from . import views
from django.contrib.auth.views  import LoginView, LogoutView

urlpatterns = [
    path('', views.listar_juegos, name='listar_juegos'),
    path('crear', views.crear_juego, name='crear_juego'),
    path('editar/<int:pk>/', views.editar_juego, name='editar_juego'),
    path('eliminar/<int:pk>/',views.eliminar_juego, name='eliminar_juego'),
    path('login/', LoginView.as_view(template_name= 'core/login.html'), name='login' ),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registro/', views.registro_usuario, name='registro'),
    path('perfil/', views.editar_perfil, name='editar_perfil'),
]