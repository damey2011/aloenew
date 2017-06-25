from django.contrib import admin

# Register your models here.
from products.models import ProductCategory

admin.site.register(ProductCategory)