from rest_framework import serializers
from .models import Product, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']  # Selecciona los campos que necesites

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()  # Anidamos el serializer de Category

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'stock', 'category', 'image']
