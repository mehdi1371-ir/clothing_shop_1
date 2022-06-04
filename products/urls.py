from django.urls import path

from .views import ProductListView, ProductDtailView

urlpatterns = [
    path('', ProductListView.as_view(), name='products'),
    path('<slug:slug>/', ProductDtailView.as_view(), name='product_detail'),
]
