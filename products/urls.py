from django.urls import path

from .views import ProductListView, ProductDetailView, CategoryListView


urlpatterns = [
    path('', ProductListView.as_view(), name='products_list'),
    path('<slug:slug>/', CategoryListView.as_view(), name='category'),
    path('detail/<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
]
