from django.views import View
from django.views.generic import (
    ListView, DetailView, TemplateView,
    CreateView, UpdateView, DeleteView
)
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from .models import Product
from .forms import ProductForm
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(View):
    def get(self, request):
        return HttpResponse("Это приложение catalog — всё работает!")

class HomeView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'

class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'

class ContactsView(TemplateView):
    template_name = 'contacts.html'


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_form.html'
    success_url = reverse_lazy('home')

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_form.html'

    def get_success_url(self):
        return reverse('product-detail', kwargs={'pk': self.object.pk})

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'product_confirm_delete.html'
    success_url = reverse_lazy('home')
