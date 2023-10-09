from django.urls import path
from .views import  *


urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),
    path('api/products/', ProductListView.as_view(), name='product-list'),
    path('api/products/', ProductListView.as_view(), name='product-list'),
  
]


