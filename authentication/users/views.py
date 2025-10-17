from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from pyexpat.errors import messages
from users.forms import SignupForm
from django.contrib.auth.forms import UserCreationForm

from users.forms import LoginForm


class Home(View):
    def get(self,request):
        return render(request,'home.html')
class Register(View):
    def get(self,request):
        form_instance=SignupForm()
        context={'form':form_instance}
        return render(request,'register.html',context)
    def post(self,request):
        form_instance=SignupForm(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('login')
        else:
            print('error')
            return render(request,'register.html',{'form':form_instance})
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
class Login(View):
    def post(self,request):
        form_instance=LoginForm(request.POST)
        if form_instance.is_valid():
            u=form_instance.cleaned_data['username']
            p=form_instance.cleaned_data['password']
            user=authenticate(username=u,password=p)
            if user:
                login(request,user)
                return redirect('home')
            else:
                messages.error(request,'invalid credentials')
                return render(request,'login.html',{'form':form_instance})

    def get(self,request):
        form_instance=LoginForm()
        context={'form':form_instance}
        return render(request,'login.html',context)
class Logout(View):
    def get(self,request):
        logout(request)
        return redirect('login')
# Create your views here.
