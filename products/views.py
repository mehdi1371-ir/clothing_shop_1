from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DeleteView

from .models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'products/products.html'
    context_object_name = 'products'


class ProductDtailView(DeleteView):
    model = Product
    template_name = 'products/products_detail.html'
    context_object_name = 'product'