from django.shortcuts import render,HttpResponse
from .utils import myFunction


# Create your views here.
def home(request):
    return render(request,"index.html")

def handle(request):
    if request.method=="POST":
        fname=request.POST.get("fname")
        lname=request.POST.get("lname")
        email=request.POST.get("email")
        if(fname=="" or lname=="" or email==""):
            return HttpResponse("Please fill all the details")
        print(fname,lname,email)
        # return HttpResponse("yo man its working")
        return HttpResponse(myFunction())
    
    return render(request,"signup.html")



