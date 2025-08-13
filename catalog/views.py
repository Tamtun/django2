from django.views import View
from django.views.generic import ListView, DetailView, TemplateView
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Product

class IndexView(View):
    def get(self, request):
        return HttpResponse("Это приложение catalog — всё работает!")

class HomeView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'

class ContactsView(TemplateView):
    template_name = 'contacts.html'
