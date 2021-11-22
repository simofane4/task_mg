from typing import ValuesView
from django.shortcuts import render

# Create your views here.



def home(request):
    return render(request,'index.html')

def event(request):
    return render(request,'event.html')

def pers(request):
    return render(request,'pers.html')


def project(request):
    return render(request,'project.html')

def task(request):
    return render(request,'task.html')

def login(request):
    return render(request,'login.html')


def register(request):
    return render(request,'register.html')


def forgotpass(request):
    return render(request,'forgot-password.html')


def project_view(request):
    return render(request,'project-view.html')

def profile(request):
    return render(request,'profile.html')