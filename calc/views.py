from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'calc.html')

def add(request):
    
    val1 = request.GET['num1']
    val2 = request.GET['num2']
    res = val1 + val2
    return render(request,'result.html',{'result':res})