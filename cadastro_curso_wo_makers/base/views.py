from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    html = '''
        <!Doctype html>
        <head>
            <title> Cursos WoMakersCode </title>
        </head>
        <body>
            <h1> Hello world </h1>
            <p> Primeiro projeto com django! </p>
        </body>
        </html>
    '''
    return HttpResponse(html)

def cadastro(request):
    pass