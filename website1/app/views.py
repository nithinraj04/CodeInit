from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return render(request,"index.html")
def work(request):
    return render(request, "working.html")
def signup(request):
    return render(request, "signupboiler.html")
