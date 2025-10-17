from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from users.forms import SignupForm


class register(View):
    def post(self,request):
        form_instance=SignupForm(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('login.html')
        else:
            print('error')
            return render(request,'register.html',{'form':form_instance})
    def get(self,request):
        form_instance=SignupForm()
        context={'form':form_instance}
        return render(request,'register.html',context)
class login(View):
    class Login(View):
        def post(self, request):
            form_instance = LoginForm(request.POST)
            if form_instance.is_valid():
                u = form_instance.cleaned_data['username']
                p = form_instance.cleaned_data['password']
                user = authenticate(username=u, password=p)
                if user:
                    login(request,user)
                    return redirect('books:home')
                else:
                    messages.error(request, 'invalid credentials')
                    return render(request, 'login.html', {'form': form_instance})

        def get(self, request):
            form_instance = LoginForm()
            context = {'form': form_instance}
            return render(request, 'login.html', context)
class logout(View):
    def get(self,request):
        logout(request)
        return redirect('login')
# Create your views here.
