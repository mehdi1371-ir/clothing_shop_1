from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import Avg
from django.http import JsonResponse

from .models import Product, Category, Rating


class ProductListView(ListView):
    model = Product
    template_name = 'products/products.html'
    context_object_name = 'all_products'


# class ProductDetailView(DetailView):
#     model = Product
#     template_name = 'products/products_detail.html'
#     context_object_name = 'product'

def product_detail(request, slug):
    product = Product.objects.get(slug=slug)
    rates = product.rates.all().aggregate(Avg('rate'))
    context = {
        'product': product,
        'rates': rates,
    }
    
    return render(request, 'products/products_detail.html', context)


def rate_image(request):
    if request.method == 'POST':
        el_id = request.POST.get('el_id')
        val = request.POST.get('val')
        obj = Rating.objects.get(id=el_id)
        obj.rate = val
        obj.save()
        return JsonResponse({'success':'true', 'rate': val}, safe=False)
    return JsonResponse({'success':'false'})

    
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