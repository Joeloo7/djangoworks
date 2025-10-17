from django.shortcuts import render,redirect

from books.forms import BookForm
from books.models import Book
from django.template.context_processors import request
from django.template.defaultfilters import title
from django.templatetags.i18n import language
from django.views import View
# def home(request):
#     return render(request,'home.html')
class Home(View):
    def get(self,request):
        return render(request,'home.html')
class Addbooks(View):
    def post(self,request):
        form_instance=BookForm(request.POST,request.FILES)
        if form_instance.is_valid():
            form_instance.save()
            # data=form_instance.cleaned_data
            # # print(data)
            # t=data['title']
            # a=data['author']
            # p=data['price']
            # pg=data['pages']
            # l=data['language']
            # b=Book.objects.create(title=t,author=a,price=p,pages=p,language=l)
            # b.save()
            return redirect('books:viewbooks')
    def get(self,request):
        form_instance=BookForm()
        context={'form':form_instance}
        return render(request, "addbooks.html",context)
class Viewbooks(View):
    def get(self,request):
        b=Book.objects.all()
        context={'books':b}
        return render(request,'viewbooks.html',context)
def edit(request,i):
    if request.method=="post":
        form_instance = BookForm(request.POST, request.FILES,instance=b)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('books:viewbooks')
    if request.method=="get":
        b=Book.objects.get(id=i)
        form_instance=BookForm(instance=b)
        context={'form':form_instance}
        return render(request,'edit.html',context)
def bookview(request,i):
    if request.method=="GET":
        b=Book.objects.get(id=i)
        context={'book':b}
        return render(request,'bookview.html',context)
def delete(request,i):
    b=Book.objects.get(id=i)
    b.delete()
    return redirect('books:viewbooks.html')
from django.db.models import Q
class search(View):
    def get(self,request):
        query = request.GET.get('q')

        if query:
            b=Book.objects.filter(Q(author__icontains=query)|Q(title__icontains=query)|Q(language__icontains=query))
            context={'book':b}
        return render(request,'search.html',context)