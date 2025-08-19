from django.urls import path, include
from .views import (
    IndexView, HomeView, ProductDetailView, ContactsView,
    ProductCreateView, ProductUpdateView, ProductDeleteView
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('index/', IndexView.as_view(), name='catalog-index'),
    path('blogs/', include('blog.urls')),
]
