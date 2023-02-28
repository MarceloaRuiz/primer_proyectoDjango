from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render


def saludo(request):
    return HttpResponse("Hola Django - Coder")

def mostrar_html(request):
    return HttpResponse("<button>este es mi boton</butonn><br><h1>Hola</h1>")

def retornar_parametro(request):
    mensaje = f"la fecha de hoy es {datetime.now()}"
    return HttpResponse(mensaje)

def mi_nombre(request, nombre):
    return HttpResponse(f"Hola, bienvenido: <b>{nombre}</b>")

def show_html(request):
    return render(request, "template1.html")