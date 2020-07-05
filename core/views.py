from django.shortcuts import render

# Create your views here.




def home (request):
    return render(request,'core/home-page.html')

def checkout(request):
    return render(request,'core/checkout-page.html')