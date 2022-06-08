from django.http import HttpResponse
from django.shortcuts import render



def home_view(request,*args,**kwargs):
    return render(request,"home.html",{})

def three_view(request,*args,**kwargs):
    return render(request,"index.html",{})

def project_view(request,*args,**kwargs):
    return render(request,"project.html",{})

def about_view(request,*args,**kwargs):
    return render(request,"about.html",{})