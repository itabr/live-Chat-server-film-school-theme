from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def chathome(request):
    return HttpResponse("<h1>Hello world</h1>")
