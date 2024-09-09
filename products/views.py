from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product

# Create your views here.
@api_view(['GET'])
def get_products(request):
    products = Product.objects.all()
    response = []
    for product in products:
        response.append({
            'id': product.id,
            'name': product.name,
            'description': product.description,
            'price': product.price,
            'stock': product.stock,
            'category': product.category,
            'image': product.image,
        })
    return Response(response, status=status.HTTP_200_OK)

