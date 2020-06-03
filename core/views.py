from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade, somar):
  soma = idade + somar
  return HttpResponse('<h1>Hello {} de {} anos e daqui {} anos tera {} anos!</h1>'.format(nome, idade, somar, soma))