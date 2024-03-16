from django.shortcuts import render,HttpResponse
from .utils import finalOutput


# Create your views here.
def home(request):
    return render(request,"index.html")

def handle(request):
    if request.method=="POST":
        input=request.POST.get("input")
        codekey=request.POST.get("codekey")
        
        
        return render(request,'signup.html',{'input': input})
    
    return render(request,"signup.html")



