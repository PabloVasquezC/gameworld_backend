from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    stock = models.IntegerField()
    category = models.CharField(max_length=255)
    image = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.name

