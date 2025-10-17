
from django.shortcuts import render,redirect
from details.models import employee
from details.forms import DetailsForm
def emplist(request):
    if (request.method=="GET"):
        e=employee.objects.all()
        context={'empl':e}
        return render(request,'emplist.html',context)
def addemp(request):
    if(request.method=="POST"):
        form_instance=DetailsForm( request.POST,request.FILES)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('emplist')
        return render(request,'addemp.html')
    if(request.method=="GET"):
        form_instance=DetailsForm()
        context={'form':form_instance}
        return render(request,'addemp.html',context)