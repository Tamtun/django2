from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from django.shortcuts import render, get_object_or_404

# Create your views here.
def index(request):
    return HttpResponse("Это приложение catalog — всё работает!")

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def contacts(request):
    return render(request, 'contacts.html')

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})