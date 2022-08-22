from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def august(request):
    return HttpResponse('<h1> August-22 app </h1>')
