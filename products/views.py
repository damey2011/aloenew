from django.shortcuts import render

# Create your views here.
from django.views import View
from rest_framework.generics import ListAPIView
from blogs.models import BlogPost
from products.models import ProductCategory
from products.serializers import ProductCategoriesSerializer


class ProductsView(View):
    def get(self, request):
        return render(request, 'products.html', {'products': 'current'})


class ProductCategoriesList(ListAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategoriesSerializer


class ProductCategoryView(View):
    def get(self, request, pk):
        posts = BlogPost.objects.filter(category=pk)
        return render(request, 'posts-results.html', {'results': posts})
