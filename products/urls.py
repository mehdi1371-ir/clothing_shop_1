from django.urls import path

from .views import ProductListView, product_detail, category, rate_image


urlpatterns = [
    path('', ProductListView.as_view(), name='products_list'),
    path('<slug:slug>/', category, name='category'),
    path('detail/<slug:slug>/', product_detail, name='product_detail'),
    path('rate/', rate_image, name='rate-view'),
]
