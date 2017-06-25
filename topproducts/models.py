from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from products.models import ProductCategory


class TopProducts(models.Model):
    title = models.CharField(max_length=200)
    details = models.TextField()
    image = models.ImageField()
    category = models.ForeignKey(to=ProductCategory, null=True)
    created_by = models.ForeignKey(User, null=True)
