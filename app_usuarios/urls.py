from django.urls import path

from .views import lista_usuarios, registro_usuario


urlpatterns = [
    path('registro/', registro_usuario, name='registro'),
    path('lista/', lista_usuarios, name='lista_usuarios'),
]