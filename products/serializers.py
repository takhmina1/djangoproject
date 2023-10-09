from rest_framework import serializers
from .models import Product, Category, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
        

class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source='category.name')
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
        
        
        
