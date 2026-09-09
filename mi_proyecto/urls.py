"""
URL configuration for mi_proyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: HttpResponse('<h1>hola estoy haciendo mi primer proyecto django</h1>')),
    path('inicio/', lambda request: HttpResponse('<p>django es un framework de desarrollo web de código abierto escrito en Python. Fue diseñado para ayudar a los desarrolladores a crear aplicaciones web de manera rápida y eficiente, siguiendo el principio de "no te repitas" (DRY, por sus siglas en inglés) y promoviendo la reutilización de código. Django proporciona una estructura sólida y herramientas integradas para manejar tareas comunes en el desarrollo web, como la gestión de bases de datos, la autenticación de usuarios, la creación de formularios y la administración del sitio web.</p>')),
]
