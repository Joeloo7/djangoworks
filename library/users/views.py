from django.http import HttpResponse
from django.shortcuts import render
def register(request):
    return render(request,'register.html')
def login(request):
    return render(request,'login.html')
def logout(request):
    return HttpResponse("logout successfully")
# Create your views here.
