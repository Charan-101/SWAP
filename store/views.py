from django.shortcuts import render
from .models import Product
# Create your views here.
def index(reuqest):
    return render(reuqest,'index.html')

def collections(reuqest):
    return render(reuqest, 'collections.html')

def loginn(reuqest):
    return render(reuqest, 'login.html')

def register(reuqest):
    return render(reuqest, 'register.html')

def product_view(request):
    return render(request, 'productview.html')