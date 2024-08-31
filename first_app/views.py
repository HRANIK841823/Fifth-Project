from django.shortcuts import render
from . forms import contactform
from . forms import studentform
from . forms import PasswordValidationProject
def home(request):
    if request.method=='POST':
        name=request.POST.get('username')
        email=request.POST.get('email')
        select=request.POST.get('select')
        return render(request,'home.html',{'name':name,'email':email,'select':select})
    else:
        return render(request,'home.html')
def about(request):
    if request.method =='POST':
        name= request.POST.get('username')
        email=request.POST.get('email')
        select=request.POST.get('select')
        return render (request, 'about.html',{'name':name ,'email':email,'select':select})
    else:
        return render (request, 'about.html')
          
def submit_form(request):
      
    return render(request,'form.html')
def DjangoForm(request):
    if request.method=='POST':
        form=contactform(request.POST,request.FILES)
        if form.is_valid():
            # file=form.cleaned_data['file']
            # with open('./first_app/upload/'+ file.name,'wb+') as destination:
            #     for chunck in file.chunks():
            #         destination.write(chunck)
            print(form.cleaned_data)
            return render(request,'django_from.html',{'form':form})
    else:
        form=contactform()
    return render(request,'django_from.html',{'form':form})

def Studentform(request):
    if request.method=='POST':
        form=studentform(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return render(request,'django_from.html',{'form':form})
    else:
        form=studentform()
    return render(request,'django_from.html',{'form':form})

def PasswordValidation(request):
    if request.method=='POST':
        form=PasswordValidationProject(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return render(request,'django_from.html',{'form':form})
    else:
        form=PasswordValidationProject()
    return render(request,'django_from.html',{'form':form})
    
def form_practise(request):
    return render(request,'form_practise.html')