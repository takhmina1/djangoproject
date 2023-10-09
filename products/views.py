from rest_framework import generics, permissions
from .serializers import ProductSerializer
from django.http import HttpResponse
from openpyxl import Workbook
from .models import Product
from django.core.cache import cache
from rest_framework import generics, permissions





class ProductListView(generics.ListAPIView):
    queryset = Product.objects.select_related('category').prefetch_related('tags')
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        cache_key = 'ProductListView'
        queryset = cache.get(cache_key)
        if not queryset:
            queryset = Product.objects.all()
            cache.set(cache_key, queryset)
        return queryset



