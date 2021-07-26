from django.http import HttpResponse
from django.shortcuts import render

def b2(request):
    return render(request, 'h1.html')

def rudra(request):
    return HttpResponse('<h1>popat</h1>')