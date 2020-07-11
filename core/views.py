from django.shortcuts import render
from django.views.generic import ListView, DetailView 
from .models import *

# Create your views here.



class home(ListView):
    model = Product
    template_name = 'core/home.html'


class product(DetailView):
    model = Product
    template_name = 'core/product.html'








def checkout(request):
    return render(request,'core/checkout.html')



def products(request):
    return render(request,'core/product.html')

