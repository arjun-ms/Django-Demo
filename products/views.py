from django.shortcuts import render
from django.http import HttpResponse
from .models import Product 
from django.shortcuts import render,redirect
from django.contrib.auth.models import auth

# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request,'products.html',{'products':products})
    # return HttpResponse("<h1>Hey!</h1>")

def about(request):
    return HttpResponse("<h1>About Me!</h1>")

def contact(request):
    return HttpResponse("<h1>Contact Me!</h1>")

def logout(request):
    
    auth.logout(request)
    return redirect('/')
