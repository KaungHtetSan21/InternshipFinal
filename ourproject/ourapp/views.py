from django.shortcuts import render
from django.shortcuts import render, redirect, HttpResponse
# Create your views here.
def homeview(request):
    return render(request, 'index.html')