from django.shortcuts import render,HttpResponse
from .utils import finalOutput


# Create your views here.
def home(request):
    return render(request,"index.html")

def handle(request):
    if request.method=="POST":
        input=request.POST.get("input")
        code=request.POST.get("codekey")
        x=request.POST.get("action")
        output=finalOutput(input, code, x)
        print(input,code)
        # output=input+ code
        return render(request,'signup.html',{'output_data': output}) 
    # output data is to be mentioned
    
    return render(request,"signup.html")


