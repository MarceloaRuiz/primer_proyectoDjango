from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hola Django - Coder")

def mostrar_html(request):
    return HttpResponse("<button>este es mi boton</butonn><br><h1>Hola</h1>")