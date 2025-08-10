from django.urls import path
from . import views

urlpatterns = [
    #path("", views.index, name="catalog-index"),
    path('', views.home, name='home'),
    path('products/<int:pk>/', views.product_detail, name='product_detail'),
    path('contacts/', views.contacts, name='contacts')
]

