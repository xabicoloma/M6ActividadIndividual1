from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
publicaciones=[
    {
        'autor':"Rodrigo",
        'titulo': "Publicacion 1",
        'contenido': "loremp ipsum",
        'fecha': "13 de julio del 2023"
    },
    {
        'autor':"Nicolas",
        'titulo': "Publicacion 2",
        'contenido': "loremp ipsum 2",
        'fecha': "13 de julio del 2023"
    },
    {
        'autor':"Adolfo",
        'titulo': "Publicacion 3",
        'contenido': "loremp ipsum 3",
        'fecha': "13 de julio del 2023"
    }
]

def bienvenida(request):
    contexto = {
        'publicaciones': publicaciones
    }
    return render(request,'home/index.html', contexto)

def contacto(request):
    return render (request, 'home/contacto.html',{'titulo': 'aweklab'})