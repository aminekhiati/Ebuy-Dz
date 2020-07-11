from django.shortcuts import render
from django.views.generic import ListView, DetailView 
from .models import *

# Create your views here.



class home(ListView):
    model = Product
    template_name = 'core/home-page.html'





# def home (request):
#     return render(request,'core/home-page.html')



def checkout(request):
    return render(request,'core/checkout-page.html')



def products(request):
    return render(request,'core/product-page.html')

