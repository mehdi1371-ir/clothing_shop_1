from django.urls import path

from .views import ProductListView, ProductDetailView, category


urlpatterns = [
    path('', ProductListView.as_view(), name='products_list'),
    path('<slug:slug>/', category, name='category'),
    path('detail/<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
]
