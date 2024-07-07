from django.shortcuts import render,HttpResponse
from .utils import finalOutput, MatrixOut, fillPrev


# Create your views here.
def home(request):
    return render(request,"signup.html")

def listToListOfList(l):
    return [list(l[i:i+5]) for i in range(0, len(l), 5)]

def handle(request):
    if request.method=="POST":
        input=request.POST.get("inputBox1")
        code=request.POST.get("inputBox2")
        x=request.POST.get("action")
        output=finalOutput(input, code, x)
        matrix = listToListOfList(MatrixOut(code))
        default = listToListOfList("ABCDEFGHIKLMNOPQRSTUVWXYZ")
        # print(input,code)
        # output=input+ code
        return render(request,'signup.html',{'output_data': output,
                                             'matrix': matrix,
                                             'default': default,
                                             'default1' : fillPrev(input, code)[0],
                                             'default2' : fillPrev(input, code)[1],
                                             }) 
    # output data is to be mentioned
    
    return render(request,"signup.html")


