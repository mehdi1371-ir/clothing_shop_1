from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView

from .models import Product, Category


class ProductListView(ListView):
    model = Product
    template_name = 'products/products.html'
    context_object_name = 'all_products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/products_detail.html'
    context_object_name = 'product'
    

# class CategoryListView(ListView):
#     template_name = 'products/category_detail.html'

#     def get_queryset(self):
#         category = get_object_or_404(Category, slug=self.kwargs['slug'])
#         self.products = category.products.all()
#         return self.products

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["products"] = self.products
#         return context
    

def category(request, slug):
    category = Category.objects.get(slug=slug)
    cat_products = category.products.all()

    context = {
        'category': category,
        'cat_products': cat_products
    }

    return render(request, 'products/category_detail.html', context)