from django.shortcuts import render,HttpResponse


# Create your views here.
def home(request):
    return render(request,"index.html")

def handle(request):
    if request.method=="POST":
        fname=request.POST.get("fname")
        lname=request.POST.get("lname")
        email=request.POST.get("email")
        print(fname,lname,email)
        return HttpResponse("yo man its working")
    
    return render(request,"signup.html")



