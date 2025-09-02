from django.views import View
from django.views.generic import (
    ListView, DetailView, TemplateView,
    CreateView, UpdateView, DeleteView
)
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy, reverse
from django.core.exceptions import PermissionDenied
from .models import Product, Category
from .forms import ProductForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .services import get_products_by_category
from django.core.cache import cache

class IndexView(View):
    def get(self, request):
        return HttpResponse("Это приложение catalog — всё работает!")

class HomeView(View):
    def get(self, request):
        products = cache.get('home_products')

        if not products:
            products = Product.objects.filter(is_published=True).select_related('category', 'owner')
            cache.set('home_products', products, timeout=60)  # кеш на 60 секунд

        return render(request, 'home.html', {'products': products})

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

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_form.html'

    def dispatch(self, request, *args, **kwargs):
        product = self.get_object()
        if product.owner != request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('product-detail', kwargs={'pk': self.object.pk})

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'product_confirm_delete.html'
    success_url = reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        product = self.get_object()
        if product.owner != request.user and not request.user.has_perm('catalog.delete_product'):
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class UnpublishProductView(LoginRequiredMixin, View):
    def post(self, request, pk):
        if not request.user.has_perm('catalog.can_unpublish_product'):
            raise PermissionDenied

        product = get_object_or_404(Product, pk=pk)
        product.is_published = False
        product.save()
        return redirect('product-detail', pk=pk)

class ProductsByCategoryView(View):
    def get(self, request, category_id):
        category = Category.objects.get(pk=category_id)
        products = get_products_by_category(category_id)
        return render(request, 'products_by_category.html', {
            'category': category,
            'products': products
        })