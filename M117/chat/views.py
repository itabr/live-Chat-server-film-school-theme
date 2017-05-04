from django.shortcuts import render , redirect
from django.http import HttpResponse

# Create your views here.


def chathome(request):
	return render(request,'chat/home.html')