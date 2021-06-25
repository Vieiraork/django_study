from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse(f'<h1>Hello World!<h1>')

def seila(request):
    return HttpResponse(f'<h1>Sei lá!<h1>')

def soma(request, n1, n2):
    return HttpResponse(f'<h1>Resultado é <strong>{n1 + n2}</strong>!<h1>')
