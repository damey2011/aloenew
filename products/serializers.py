from rest_framework import serializers
from products.models import ProductCategory


class ProductCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = "__all__"
