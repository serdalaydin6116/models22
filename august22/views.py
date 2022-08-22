from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def august(request):
    return HttpResponse('<h1> This is models study with direct url from project-August22 </h1>')
