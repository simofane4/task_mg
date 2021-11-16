from django.shortcuts import render

# Create your views here.



def home(request):
    return render(request,'index.html')

def event(request):
    return render(request,"event.html")

def pers(request):
    return render(request,'pers.html')
