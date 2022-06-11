from django import views
from django.urls import path

from .views import ProductListView, CategoryListView, ProductDetailView

urlpatterns = [
    path('products/', ProductListView.as_view(), name='products'),
    path('category/<slug:slug>/', CategoryListView.as_view(), name='category'),
    path('details/<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
]
