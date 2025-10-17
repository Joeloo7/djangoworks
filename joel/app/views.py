from django.shortcuts import render
from django.http import HttpResponse
def first(request):
    return render(request,'second.html')
# Create your views here.
def second(request):
    return render(request,'second.html')