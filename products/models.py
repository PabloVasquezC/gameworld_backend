from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    # models.ImageField(_(""), upload_to=None, height_field=None, width_field=None, max_length=None)
    price = models.FloatField()
    stock = models.IntegerField()
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.name

