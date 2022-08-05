from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, dia):
    return HttpResponse('<h1>Hello {}, Hoje é dia {}</h1>'.format(nome, dia))