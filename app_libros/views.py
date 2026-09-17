from html import escape
from random import sample

from django.http import HttpResponse

LIBROS = [
	('978-8497592208', 'Cien años de soledad', 'La historia de la familia Buendía en Macondo.', 'Realismo mágico'),
	('978-8420412146', 'Don Quijote de la Mancha', 'Aventuras de un hidalgo que decide convertirse en caballero.', 'Clásico'),
	('978-8437604947', 'La sombra del viento', 'Un misterio literario ambientado en la Barcelona de posguerra.', 'Misterio'),
	('978-8491050294', 'El principito', 'Un viaje poético sobre la amistad, el amor y la responsabilidad.', 'Fábula'),
	('978-8423337176', '1984', 'Una novela sobre vigilancia, control y libertad individual.', 'Distopía'),
	('978-8437604565', 'Rayuela', 'Una novela experimental que invita a múltiples formas de lectura.', 'Literatura'),
	('978-8466348386', 'La casa de los espíritus', 'Saga familiar marcada por cambios políticos y secretos.', 'Realismo mágico'),
	('978-8497592581', 'Fahrenheit 451', 'Un futuro donde los libros están prohibidos y pensar es peligroso.', 'Ciencia ficción'),
	('978-8420651928', 'El nombre de la rosa', 'Investigación de una serie de crímenes en una abadía medieval.', 'Histórica'),
	('978-8499088077', 'Sapiens', 'Una mirada amplia a la historia de la humanidad.', 'Ensayo'),
	('978-8420471830', 'El amor en los tiempos del cólera', 'Una historia de amor persistente a través de los años.', 'Novela'),
	('978-8437606781', 'Pedro Páramo', 'Un hombre llega a Comala buscando el origen de su historia familiar.', 'Realismo mágico'),
	('978-8490321594', 'El hobbit', 'La aventura de Bilbo Bolsón para recuperar un tesoro custodiado por un dragón.', 'Fantasía'),
	('978-8420684781', 'Matar a un ruiseñor', 'Una historia sobre justicia, empatía y crecimiento en una comunidad sureña.', 'Drama'),
	('978-8497593069', 'Crónica de una muerte anunciada', 'La reconstrucción de un crimen que todo un pueblo parecía conocer.', 'Novela'),
]


def lista_libros(request):
	libros_seleccionados = sample(LIBROS, 10)
	tarjetas = ''.join(
		f"""<div class="col-md-6 col-xl-4"><article class="card h-100 border-0 shadow-sm">
<div class="card-body"><span class="badge text-bg-info mb-2">{escape(categoria)}</span>
<h2 class="h5 fw-bold">{escape(titulo)}</h2><p class="text-secondary">{escape(descripcion)}</p>
<p class="small text-muted mb-0"><strong>ISBN:</strong> {escape(isbn)}</p></div></article></div>"""
		for isbn, titulo, descripcion, categoria in libros_seleccionados
	)
	html = f"""<!doctype html><html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1"><title>Catálogo | Pr Biblioteca</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
<style>body {{ background:#f4f7fb; }} .intro {{ background:#12355b; color:white; }}</style></head><body>
<nav class="navbar navbar-expand-lg navbar-dark bg-dark"><div class="container"><a class="navbar-brand fw-bold" href="/">Pr Biblioteca</a>
<div class="navbar-nav ms-auto"><a class="nav-link" href="/usuarios/registro/">Registrar</a><a class="nav-link" href="/usuarios/lista/">Usuarios</a><a class="nav-link active" href="/libros/">Libros</a></div></div></nav>
<main class="container py-5"><section class="intro rounded-4 p-4 p-md-5 mb-4"><p class="text-uppercase small fw-semibold">Catálogo disponible</p><h1 class="display-6 fw-bold">Libros para descubrir</h1><p class="lead mb-0">Consulta ISBN, categoría y descripción de cada título.</p></section>
<div class="row g-4">{tarjetas}</div></main></body></html>"""
	return HttpResponse(html)
