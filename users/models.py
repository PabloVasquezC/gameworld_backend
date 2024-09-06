from django.db import models

class User(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    address = models.TextField(max_length=255)
    phone = models.CharField(max_length=15, default=False) 
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # models.ImageField(_(""), upload_to=None, height_field=None, width_field=None, max_length=None)

