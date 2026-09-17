from html import escape

from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.middleware.csrf import get_token

usuarios_registrados = []


def _layout(titulo, contenido):
	return f"""<!doctype html>
<html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(titulo)} | Pr Biblioteca</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
<style>body {{ background:#f4f7fb; }} .navbar-brand {{ letter-spacing:.04em; }} .panel {{ max-width:760px; }}</style>
</head><body>
<nav class="navbar navbar-expand-lg navbar-dark bg-dark"><div class="container">
<a class="navbar-brand fw-bold" href="/">Pr Biblioteca</a>
<div class="navbar-nav ms-auto"><a class="nav-link" href="/usuarios/registro/">Registrar</a>
<a class="nav-link" href="/usuarios/lista/">Usuarios</a><a class="nav-link" href="/libros/">Libros</a></div>
</div></nav><main class="container py-5"><div class="panel mx-auto">{contenido}</div></main></body></html>"""


def registro_usuario(request):
	if request.method == 'POST':
		nombre = request.POST.get('nombre', '').strip()
		correo = request.POST.get('correo', '').strip()
		telefono = request.POST.get('telefono', '').strip()
		if nombre and correo:
			usuarios_registrados.append({
				'nombre': nombre,
				'correo': correo,
				'telefono': telefono,
			})
			return redirect('lista_usuarios')

	csrf_token = get_token(request)
	contenido = f"""<div class="card border-0 shadow-sm"><div class="card-body p-4 p-md-5">
<h1 class="h2 fw-bold mb-2">Registro de usuario</h1>
<p class="text-secondary mb-4">Completa tus datos para usar los servicios de la biblioteca.</p>
<form method="post" novalidate><input type="hidden" name="csrfmiddlewaretoken" value="{csrf_token}">
<div class="mb-3"><label class="form-label" for="nombre">Nombre completo</label>
<input class="form-control" id="nombre" name="nombre" required></div>
<div class="mb-3"><label class="form-label" for="correo">Correo electrónico</label>
<input class="form-control" type="email" id="correo" name="correo" required></div>
<div class="mb-3"><label class="form-label" for="telefono">Teléfono</label>
<input class="form-control" id="telefono" name="telefono"></div>
<div class="alert alert-info"><strong>Reglas:</strong> cuidar los libros, respetar la fecha de devolución y mantener actualizados tus datos.</div>
<button class="btn btn-primary" type="submit">Guardar registro</button>
<a class="btn btn-outline-secondary ms-2" href="/">Cancelar</a>
</form></div></div>"""
	return HttpResponse(_layout('Registro', contenido))


def lista_usuarios(request):
	if usuarios_registrados:
		filas = ''.join(
			f"<tr><td>{escape(usuario['nombre'])}</td><td>{escape(usuario['correo'])}</td>"
			f"<td>{escape(usuario['telefono']) or 'No indicado'}</td></tr>"
			for usuario in usuarios_registrados
		)
		contenido = f"""<div class="card border-0 shadow-sm"><div class="card-body p-4">
<div class="d-flex justify-content-between align-items-center mb-3"><h1 class="h2 mb-0">Usuarios registrados</h1>
<a class="btn btn-primary" href="{reverse('registro')}">Nuevo usuario</a></div>
<div class="table-responsive"><table class="table align-middle"><thead><tr><th>Nombre</th><th>Correo</th><th>Teléfono</th></tr></thead><tbody>{filas}</tbody></table></div>
</div></div>"""
	else:
		contenido = """<div class="card border-0 shadow-sm text-center"><div class="card-body p-5">
<h1 class="h2">Aún no hay usuarios</h1><p class="text-secondary">Registra el primer usuario de la biblioteca.</p>
<a class="btn btn-primary" href="/usuarios/registro/">Registrar usuario</a></div></div>"""
	return HttpResponse(_layout('Usuarios', contenido))
