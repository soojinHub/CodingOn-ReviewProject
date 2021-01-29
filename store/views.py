from django.shortcuts import render, redirect
from django.http.response import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')
def menu(request):
    return render(request, 'menu.html')

def review(request):
    return render(request, 'review.html')

def info(request):
    return render(request, 'info.html')

def purchase(request):
    return render(request, 'purchase.html')
