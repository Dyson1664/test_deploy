from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'home.html')

def john(request):
    return HttpResponse('Hiya johnnnnnn')

def capitals(request):
    return render(request, 'capitals.html')