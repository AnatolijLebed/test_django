from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Страница приложения app")
def categories(request, catid):
    if(request.GET):
        print(request.GET)
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>{catid}</p>')
def archive(request, year):
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>{year}</p>')

# Create your views here.
