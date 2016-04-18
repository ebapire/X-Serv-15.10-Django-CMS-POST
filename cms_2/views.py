from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from models import Contenido
from django.http import HttpResponse
from django.template import loader, Context

# Create your views here.

def personas (request):
    lista_usuarios = Contenido.objects.all()
    respuesta = "Se ha introducido contenido con los nombres: <ol>"
    for usuario in lista_usuarios:
        respuesta += '<li><a href='+ str(usuario.id) + '>' + usuario.nombre + '</a>'
    respuesta += "</ol>"
    return HttpResponse(respuesta)
@csrf_exempt
def persona (request, identif):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        contenido = request.POST['contenido']
        new = Contenido(nombre = nombre, contenido = contenido)
        new.save()
        respuesta = nombre + " ha introducido nuevo contendido"
        respuesta += "<br><a href=/> Ve al inicio</a>"
        return HttpResponse(respuesta)

    try:
        content = Contenido.objects.get(id=identif)
    except Contenido.DoesNotExist:
        return HttpResponse ("Nadie ha introducido contenido con ese id")
    respuesta = "Nombre: " + content.nombre

    respuesta += "<p> Todo el contenido introducido por ese usuario: <ul>"
    contenidos_usuario = Contenido.objects.filter(nombre=content.nombre)
    for cont in contenidos_usuario:
        respuesta += "<li>" + cont.contenido
    respuesta += "</ul>"

    if request.user.is_authenticated():
        logg = '<p>Te has conectado como ' + request.user.username
        logg += '<br><a href=/logout> Desconectarse</a>'
    else:
        logg = '<p>No estas conectado '
        logg += '<br><a href=/login> Conectate</a>'

    template = loader.get_template("plantilla.html")
    contexto = {'contenido': respuesta, 'loggeado': logg}

    return HttpResponse(template.render(Context(contexto)))

def usuario (request):
    respuesta = "Te has conectado como " + request.user.username
    respuesta += "<br><a href=/> Ve al inicio</a>"
    return HttpResponse(respuesta)
