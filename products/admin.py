from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')  # Muestra estos campos en la lista
    search_fields = ('name',)  # Añade una barra de búsqueda por nombre
    list_filter = ('category',)  # Filtro por categoría

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)