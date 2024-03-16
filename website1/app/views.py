from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return render(request,"index.html")

def signup(request):
    return render(request,"signup.html")



