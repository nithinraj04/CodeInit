from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return render(request,"index.html")

def handle(request):
    if request.method=="POST":
        
        return HttpResponse("yo man its working")
    return render(request,"signup.html")



