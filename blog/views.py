from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('HELLO WORLD')


def posts(request):
    return render(request, 'blog/index.html')


def about(request):
    return render(request, 'blog/sobre.html')

