from django.urls import path
from .views import IndexView, HomeView, ProductDetailView, ContactsView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('index/', IndexView.as_view(), name='catalog-index'),
    path('blogs/', include('blog.urls')),
]
