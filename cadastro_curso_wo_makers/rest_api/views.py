from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
# Ira implementar uma view onde é possivel obter essa mensagem de hello world api através de uma requisição get
# e também enviar um nome para receber uma mensagem personalizada através do POST
@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'POST':
        return Response({'message': f'Hello, {request.data.get("name")}'})
    return Response({'hello': 'WORLD API'})
