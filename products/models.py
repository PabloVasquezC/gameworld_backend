from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    stock = models.IntegerField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    image = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name    

