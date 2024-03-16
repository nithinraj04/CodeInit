from django.shortcuts import render,HttpResponse


# Create your views here.
def home(request):
    return render(request,"index.html")

def handle(request):
    if request.method=="POST":
        fname=request.POST.get("fname")
        lname=request.POST.get("lname")
        email=request.POST.get("email")
        output_data=fname+' '+lname
        print(fname,lname,email)
        return render(request,'signup.html',{'output_data': output_data})
    
    return render(request,"signup.html")



